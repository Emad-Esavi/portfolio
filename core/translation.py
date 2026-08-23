from modeltranslation.translator import TranslationOptions, register

from .models import Profile, Project, Service


@register(Profile)
class ProfileTranslationOptions(TranslationOptions):
    fields = (
        "full_name",
        "job_title",
        "short_bio",
        "about",
        "location",
        "seo_title",
        "seo_description",
    )


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "short_description",
        "description",
    )


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "short_description",
        "description",
    )
