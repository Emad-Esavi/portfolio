from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from modeltranslation.admin import TabbedTranslationAdmin

from .models import Category, Post, Tag


@admin.register(Category)
class CategoryAdmin(TabbedTranslationAdmin):
    list_display = ("name", "slug", "post_count")
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}

    @admin.display(description="Posts")
    def post_count(self, obj):
        return obj.posts.count()


@admin.register(Tag)
class TagAdmin(TabbedTranslationAdmin):
    list_display = ("name", "slug", "post_count")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}

    @admin.display(description="Posts")
    def post_count(self, obj):
        return obj.posts.count()


@admin.action(description="Mark selected posts as Published")
def mark_published(modeladmin, request, queryset):
    now = timezone.now()
    
    queryset.filter(published_at__isnull=True).update(published_at=now)
    updated = queryset.update(status=Post.Status.PUBLISHED)
    modeladmin.message_user(request, f"{updated} post(s) marked as published.")


@admin.action(description="Mark selected posts as Draft")
def mark_draft(modeladmin, request, queryset):
    updated = queryset.update(status=Post.Status.DRAFT)
    modeladmin.message_user(request, f"{updated} post(s) marked as draft.")


@admin.register(Post)
class PostAdmin(TabbedTranslationAdmin):
    save_on_top = True
    list_display = (
        "title",
        "category",
        "status",
        "is_featured",
        "published_at",
        "view_count",
        "reading_time_display",
        "image_preview",
    )
    list_filter = (
        "status",
        "is_featured",
        "category",
        "tags",
        "published_at",
    )
    list_editable = (
        "status",
        "is_featured",
    )
    search_fields = (
        "title",
        "excerpt",
        "content",
        "author_name",
    )
    prepopulated_fields = {
        "slug": ("title",),
    }
    filter_horizontal = ("tags",)
    date_hierarchy = "published_at"
    readonly_fields = (
        "view_count",
        "created_at",
        "updated_at",
        "image_preview",
    )
    actions = [mark_published, mark_draft]
    ordering = ("-published_at", "-created_at")

    fieldsets = (
        ("Content", {
            "fields": (
                "title",
                "slug",
                "excerpt",
                "content",
            ),
        }),
        ("Media", {
            "fields": (
                "featured_image",
                "featured_image_url",
                "featured_image_alt",
                "image_preview",
            ),
        }),
        ("Organization", {
            "fields": (
                "category",
                "tags",
                "author_name",
            ),
        }),
        ("Publishing", {
            "fields": (
                "status",
                "is_featured",
                "published_at",
            ),
        }),
        ("SEO", {
            "fields": (
                "seo_title",
                "seo_description",
            ),
        }),
        ("Stats", {
            "fields": (
                "view_count",
                "created_at",
                "updated_at",
            ),
        }),
    )

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if obj is None:
            fieldsets = [fs for fs in fieldsets if fs[0] != "Stats"]
        return fieldsets

    @admin.display(description="Reading time")
    def reading_time_display(self, obj):
        return f"{obj.reading_time} min"

    @admin.display(description="Image")
    def image_preview(self, obj):
        url = obj.image_url
        if not url:
            return "—"
        return format_html(
            '<img src="{}" alt="{}" style="max-height:60px;border-radius:6px;" />',
            url,
            obj.featured_image_alt or obj.title,
        )
