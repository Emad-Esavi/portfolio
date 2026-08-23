import mimetypes

from django.contrib import messages
from django.core.paginator import Paginator
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.text import get_valid_filename
from django.utils.translation import gettext as _
from django.views.decorators.http import require_GET, require_POST
from django_ratelimit.decorators import ratelimit

from blog.models import Post

from .forms import ContactForm
from .models import (
    Certificate,
    ContactMessage,
    Experience,
    Profile,
    Project,
    Service,
    Skill,
)
from .emails import send_contact_notification
from .utils import get_client_ip


@require_GET
def download_resume(request):
    profile = Profile.objects.first()
    if not profile or not profile.resume:
        raise Http404(_("Resume not available."))

    resume = profile.resume
    extension = resume.name.rsplit(".", 1)[-1].lower() if "." in resume.name else "pdf"
    filename = get_valid_filename(f"CV.{extension}") or "CV.pdf"
    content_type, _ = mimetypes.guess_type(resume.name)
    if not content_type:
        content_type = "application/octet-stream"

    return FileResponse(
        resume.open("rb"),
        as_attachment=True,
        filename=filename,
        content_type=content_type,
    )


def home(request):
    profile = Profile.objects.first()
    certificates = Certificate.objects.filter(is_featured=True)
    skills = Skill.objects.filter(is_featured=True)
    projects = (
        Project.objects.filter(is_featured=True)
        .prefetch_related("skills")
    )
    experiences = Experience.objects.all()
    latest_posts = (
        Post.published()
        .select_related("category")
        .prefetch_related("tags")[:3]
    )

    return render(request, "core/home.html", {
        "profile": profile,
        "certificates": certificates,
        "skills": skills,
        "projects": projects,
        "experiences": experiences,
        "latest_posts": latest_posts,
        "form": ContactForm(initial={"variant": "home"}),
    })


def projects(request):
    profile = Profile.objects.first()
    status = request.GET.get("status", "").strip()
    qs = Project.objects.prefetch_related("skills").all()

    if status in {choice[0] for choice in Project.STATUS_CHOICES}:
        qs = qs.filter(status=status)

    paginator = Paginator(qs, 9)
    page_obj = paginator.get_page(request.GET.get("page"))

    return render(request, "core/projects.html", {
        "profile": profile,
        "page_obj": page_obj,
        "projects": page_obj.object_list,
        "current_status": status,
        "status_choices": Project.STATUS_CHOICES,
    })


def project_detail(request, slug):
    profile = Profile.objects.first()
    project = get_object_or_404(
        Project.objects.prefetch_related("skills", "images"),
        slug=slug,
    )
    related = list(
        Project.objects.prefetch_related("skills")
        .exclude(pk=project.pk)
        .filter(status=project.status)[:3]
    )
    if len(related) < 3:
        extra = list(
            Project.objects.prefetch_related("skills")
            .exclude(pk=project.pk)
            .exclude(pk__in=[p.pk for p in related])[: 3 - len(related)]
        )
        related = related + extra

    return render(request, "core/project_detail.html", {
        "profile": profile,
        "project": project,
        "related_projects": related,
    })


def certificates(request):
    profile = Profile.objects.first()
    certificates_qs = Certificate.objects.all()

    return render(request, "core/certificates.html", {
        "profile": profile,
        "certificates": certificates_qs,
    })


def about(request):
    profile = Profile.objects.first()
    skills = Skill.objects.filter(is_featured=True)
    experiences = Experience.objects.all()[:4]

    return render(request, "core/about.html", {
        "profile": profile,
        "skills": skills,
        "experiences": experiences,
    })


def services(request):
    profile = Profile.objects.first()
    services_qs = Service.objects.filter(is_active=True).prefetch_related("skills")

    return render(request, "core/services.html", {
        "profile": profile,
        "services": services_qs,
    })


def contact(request):
    profile = Profile.objects.first()

    return render(request, "core/contact.html", {
        "profile": profile,
        "form": ContactForm(initial={"variant": "page"}),
    })


@require_POST
@ratelimit(key="ip", rate="5/h", method="POST", block=False)
def contact_submit(request):
    variant = request.POST.get("variant") or "page"
    if variant not in {"home", "page"}:
        variant = "page"

    if getattr(request, "limited", False):
        form = ContactForm(request.POST)
        # Keep variant even if the bound form is invalid.
        context = {
            "form": form,
            "variant": variant,
            "rate_limited": True,
            "form_error": _(
                "Too many messages. Please wait an hour before trying again."
            ),
        }
        if request.htmx:
            return render(
                request,
                "core/partials/contact_form.html",
                context,
                status=429,
            )
        messages.error(request, context["form_error"])
        return redirect("contact")

    form = ContactForm(request.POST)
    if form.is_valid():
        if form.is_honeypot_triggered():
            if request.htmx:
                return render(
                    request,
                    "core/partials/contact_success.html",
                    {"variant": form.cleaned_data.get("variant") or variant},
                )
            messages.success(
                request,
                _("Thank you! Your message has been sent."),
            )
            return redirect("contact")

        contact_message = ContactMessage.objects.create(
            name=form.cleaned_data["name"],
            email=form.cleaned_data["email"],
            subject=form.cleaned_data["subject"],
            message=form.cleaned_data["message"],
            company=form.cleaned_data["company"],
            phone=form.cleaned_data["phone"],
            ip_address=get_client_ip(request),
        )
        send_contact_notification(contact_message)

        if request.htmx:
            return render(
                request,
                "core/partials/contact_success.html",
                {"variant": form.cleaned_data.get("variant") or variant},
            )
        messages.success(request, _("Thank you! Your message has been sent."))
        return redirect("contact")

    context = {
        "form": form,
        "variant": form.data.get("variant") or variant,
    }
    if request.htmx:
        return render(
            request,
            "core/partials/contact_form.html",
            context,
            status=422,
        )
    messages.error(request, _("Please correct the errors below."))
    return redirect("contact")
