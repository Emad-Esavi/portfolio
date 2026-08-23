from modeltranslation.translator import TranslationOptions, register

from .models import Category, Post, Tag


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "excerpt",
        "content",
        "featured_image_alt",
        "seo_title",
        "seo_description",
    )


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = (
        "name",
        "description",
    )


@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ("name",)
