import logging

from celery import shared_task
from django.core.exceptions import ObjectDoesNotExist

from .emails import send_contact_notification
from .models import ContactMessage

logger = logging.getLogger(__name__)


@shared_task(
    bind=True,
    autoretry_for=(Exception,),
    retry_backoff=True,
    retry_kwargs={"max_retries": 5},
)
def send_contact_notification_task(self, contact_message_id: int) -> bool:
    try:
        contact_message = ContactMessage.objects.get(pk=contact_message_id)
    except ObjectDoesNotExist:
        logger.warning(
            "Contact notification skipped: message id=%s no longer exists.",
            contact_message_id,
        )
        return False

    return send_contact_notification(contact_message)
