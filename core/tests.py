from unittest.mock import patch

from django.core import mail
from django.test import Client, TestCase, override_settings
from django.urls import reverse

from .models import ContactMessage, Profile
from .tasks import send_contact_notification_task


@override_settings(
    EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend",
    CELERY_TASK_ALWAYS_EAGER=True,
    CELERY_TASK_EAGER_PROPAGATES=True,
)
class ContactEmailQueueTests(TestCase):
    def setUp(self):
        self.client = Client()
        Profile.objects.create(
            full_name="Site Owner",
            job_title="Developer",
            short_bio="Bio",
            email="owner@example.com",
        )

    @patch("core.views.send_contact_notification_task.delay")
    def test_contact_submit_enqueues_notification_task(self, mock_delay):
        response = self.client.post(
            reverse("contact_submit"),
            {
                "name": "Jane Doe",
                "email": "jane@example.com",
                "subject": "Hello",
                "message": "This is a test message.",
                "variant": "page",
            },
        )

        self.assertEqual(response.status_code, 302)
        contact_message = ContactMessage.objects.get()
        mock_delay.assert_called_once_with(contact_message.pk)

    def test_contact_notification_task_sends_email_when_eager(self):
        contact_message = ContactMessage.objects.create(
            name="Jane Doe",
            email="jane@example.com",
            subject="Hello",
            message="This is a test message.",
        )

        result = send_contact_notification_task.delay(contact_message.pk)

        self.assertTrue(result.result)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, ["owner@example.com"])
        self.assertEqual(mail.outbox[0].reply_to, ["jane@example.com"])

    def test_contact_notification_task_skips_missing_message(self):
        result = send_contact_notification_task.delay(99999)

        self.assertFalse(result.result)
        self.assertEqual(len(mail.outbox), 0)
