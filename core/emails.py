import logging

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.translation import gettext as _

from .models import ContactMessage, Profile

logger = logging.getLogger(__name__)


def send_contact_notification(contact_message: ContactMessage) -> bool:
    """
    Email the site owner when a new contact message is submitted.
    Returns True if the email was sent, False if skipped or failed.
    """
    profile = Profile.objects.first()
    if not profile or not profile.email:
        logger.warning(
            "Contact notification skipped: no profile email configured in the database."
        )
        return False

    subject = contact_message.subject.strip() or _("No Subject")
    email_subject = _("New contact message: %(subject)s") % {"subject": subject}

    context = {
        "contact_message": contact_message,
        "profile": profile,
        "subject_display": subject,
        "submitted_at": timezone.localtime(contact_message.created_at),
    }

    html_body = render_to_string(
        "core/emails/contact_notification.html",
        context,
    )
    text_body = render_to_string(
        "core/emails/contact_notification.txt",
        context,
    )

    message = EmailMultiAlternatives(
        subject=email_subject,
        body=text_body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[profile.email],
        reply_to=[contact_message.email],
    )
    message.attach_alternative(html_body, "text/html")

    try:
        message.send(fail_silently=False)
    except Exception:
        logger.exception(
            "Failed to send contact notification for message id=%s",
            contact_message.pk,
        )
        return False

    return True
