from django import forms
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):
    name = forms.CharField(
        label=_("Full Name"),
        max_length=150,
        error_messages={
            "required": _("Please enter your name."),
            "max_length": _("Name must be at most 150 characters."),
        },
    )
    email = forms.EmailField(
        label=_("Email Address"),
        error_messages={
            "required": _("Please enter your email address."),
            "invalid": _("Enter a valid email address."),
        },
    )
    subject = forms.CharField(
        label=_("Subject"),
        max_length=200,
        required=False,
        error_messages={
            "max_length": _("Subject must be at most 200 characters."),
        },
    )
    company = forms.CharField(
        label=_("Company"),
        max_length=150,
        required=False,
        error_messages={
            "max_length": _("Company must be at most 150 characters."),
        },
    )
    phone = forms.CharField(
        label=_("Phone"),
        max_length=30,
        required=False,
        error_messages={
            "max_length": _("Phone must be at most 30 characters."),
        },
    )
    message = forms.CharField(
        label=_("Message"),
        min_length=10,
        max_length=5000,
        widget=forms.Textarea,
        error_messages={
            "required": _("Please enter a message."),
            "min_length": _("Message must be at least 10 characters."),
            "max_length": _("Message must be at most 5000 characters."),
        },
    )
    
    website = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
    )
    variant = forms.ChoiceField(
        choices=(("home", "home"), ("page", "page")),
        required=False,
        initial="page",
        widget=forms.HiddenInput,
    )

    def clean_name(self):
        return self.cleaned_data["name"].strip()

    def clean_subject(self):
        return (self.cleaned_data.get("subject") or "").strip()

    def clean_company(self):
        return (self.cleaned_data.get("company") or "").strip()

    def clean_phone(self):
        return (self.cleaned_data.get("phone") or "").strip()

    def clean_message(self):
        return self.cleaned_data["message"].strip()

    def is_honeypot_triggered(self):
        return bool((self.cleaned_data.get("website") or "").strip())
