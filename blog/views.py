from django.core.paginator import Paginator
from django.db.models import F, Q
from django.shortcuts import get_object_or_404, render
from django.utils.translation import gettext as _

from core.models import Profile

from .models import Category, Post, Tag


def _base_context():
    return {
        "profile": Profile.objects.first(),
        "categories": Category.objects.all(),
    }


def _published_queryset():
    return (
        Post.published()
        .select_related("category")
        .prefetch_related("tags")
    )


def post_list(request):
    qs = _published_queryset()
    q = request.GET.get("q", "").strip()
    if q:
        qs = qs.filter(
            Q(title__icontains=q)
            | Q(excerpt__icontains=q)
            | Q(content__icontains=q)
        )

    featured_posts = []
    if not q:
        featured_posts = list(qs.filter(is_featured=True)[:3])

    paginator = Paginator(qs, 6)
    page_obj = paginator.get_page(request.GET.get("page"))

    context = _base_context()
    context.update({
        "page_obj": page_obj,
        "posts": page_obj.object_list,
        "featured_posts": featured_posts,
        "search_query": q,
        "active_category": None,
        "active_tag": None,
        "list_title": _("Blog"),
        "list_subtitle": _(
            "Articles, notes, and write-ups on backend development, "
            "APIs, and building reliable systems."
        ),
    })
    return render(request, "blog/post_list.html", context)


def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    qs = _published_queryset().filter(category=category)

    paginator = Paginator(qs, 6)
    page_obj = paginator.get_page(request.GET.get("page"))

    context = _base_context()
    context.update({
        "page_obj": page_obj,
        "posts": page_obj.object_list,
        "featured_posts": [],
        "search_query": "",
        "active_category": category,
        "active_tag": None,
        "list_title": category.name,
        "list_subtitle": category.description or _(
            "Posts filed under %(category)s."
        ) % {"category": category.name},
    })
    return render(request, "blog/post_list.html", context)


def tag_posts(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    qs = _published_queryset().filter(tags=tag)

    paginator = Paginator(qs, 6)
    page_obj = paginator.get_page(request.GET.get("page"))

    context = _base_context()
    context.update({
        "page_obj": page_obj,
        "posts": page_obj.object_list,
        "featured_posts": [],
        "search_query": "",
        "active_category": None,
        "active_tag": tag,
        "list_title": f"#{tag.name}",
        "list_subtitle": _("Posts tagged with %(tag)s.") % {"tag": tag.name},
    })
    return render(request, "blog/post_list.html", context)


def post_detail(request, slug):
    qs = Post.objects.select_related("category").prefetch_related("tags")

    if request.user.is_staff:
        post = get_object_or_404(qs, slug=slug)
    else:
        post = get_object_or_404(qs, slug=slug, status=Post.Status.PUBLISHED)

    Post.objects.filter(pk=post.pk).update(view_count=F("view_count") + 1)
    post.refresh_from_db(fields=["view_count"])

    related = []
    if post.category_id:
        related = list(
            _published_queryset()
            .filter(category_id=post.category_id)
            .exclude(pk=post.pk)[:3]
        )
    if len(related) < 3:
        extra = list(
            _published_queryset()
            .exclude(pk=post.pk)
            .exclude(pk__in=[p.pk for p in related])[: 3 - len(related)]
        )
        related = related + extra

    context = _base_context()
    context.update({
        "post": post,
        "related_posts": related,
    })
    return render(request, "blog/post_detail.html", context)
