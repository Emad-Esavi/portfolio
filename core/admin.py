from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import (
    Profile,
    Skill,
    Project,
    ProjectImage,
    Experience,
    Service,
    Certificate,
    ContactMessage,
)

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(TranslationAdmin):
    list_display = (
        "full_name",
        "job_title",
        "updated_at",
    )
    search_fields = (
        "full_name",
        "job_title",
    )

    fieldsets = (
        ("Basic Information", {
            "fields": (
                "full_name",
                "job_title",
                "short_bio",
                "about",
                "location",
                "email",
                "phone",
            )
        }),
        ("Media", {
            "fields": (
                "profile_image",
                "resume",
            )
        }),
        ("Social Links", {
            "fields": (
                "github",
                "linkedin",
                "instagram",
                "x",
            )
        }),
        ("SEO", {
            "fields": (
                "seo_title",
                "seo_description",
            )
        }),
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "is_featured",
    )

    list_editable = (
        "is_featured",
    )

    list_filter = (
        "is_featured",
    )

    search_fields = (
        "name",
    )

    ordering = (
        "name",
    )
    

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    


@admin.register(Project)
class ProjectAdmin(TranslationAdmin):
    list_display = (
        "title",
        "status",
        "is_featured",
        "display_order",
        "created_at",
    )

    list_filter = (
        "status",
        "is_featured",
    )

    list_editable = (
        "is_featured",
        "display_order",
    )

    search_fields = (
        "title",
        "short_description",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    filter_horizontal = (
        "skills",
    )

    ordering = (
        "display_order",
        "-created_at",
    )
    
    inlines = [
        ProjectImageInline
    ]
    
    
@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = (
        "project",
        "display_order",
    )
    
    
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "position",
        "company",
        "employment_type",
        "currently_working",
        "start_date",
        "end_date",
    )

    list_filter = (
        "employment_type",
        "currently_working",
    )

    list_editable = (
        "currently_working",
    )

    search_fields = (
        "position",
        "company",
    )

    ordering = (
        "display_order",
        "-start_date",
    )
    
    
    
@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    list_display = (
        "title",
        "icon",
        "is_active",
        "display_order",
    )

    list_editable = (
        "is_active",
        "display_order",
    )

    list_filter = (
        "is_active",
        "icon",
    )

    search_fields = (
        "title",
        "short_description",
    )

    filter_horizontal = (
        "skills",
    )

    ordering = (
        "display_order",
        "title",
    )

    fieldsets = (
        (None, {
            "fields": (
                "title",
                "short_description",
                "description",
                "icon",
                "image",
                "skills",
            )
        }),
        ("Display", {
            "fields": (
                "is_active",
                "display_order",
            )
        }),
    )


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "issuer",
        "issued_on",
        "is_featured",
        "display_order",
    )

    list_filter = (
        "issuer",
        "is_featured",
        "issued_on",
    )

    list_editable = (
        "is_featured",
        "display_order",
    )

    search_fields = (
        "title",
        "issuer",
        "credential_id",
        "description",
    )

    ordering = (
        "display_order",
        "-issued_on",
    )

    fieldsets = (
        ("Certificate", {
            "fields": (
                "title",
                "issuer",
                "description",
                "image",
            )
        }),
        ("Credential", {
            "fields": (
                "credential_url",
                "credential_id",
                "issued_on",
            )
        }),
        ("Display", {
            "fields": (
                "is_featured",
                "display_order",
            )
        }),
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "company",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "company",
        "subject",
        "message",
    )

    readonly_fields = (
        "created_at",
        "replied_at",
        "ip_address",
    )

    ordering = (
        "-created_at",
    )