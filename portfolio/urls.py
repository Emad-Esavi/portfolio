"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
"""
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from blog.sitemaps import PostSitemap

sitemaps = {
    "posts": PostSitemap,
}

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    path("api/", include("blog.api.urls")),
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="robots.txt",
            content_type="text/plain",
        ),
        name="robots_txt",
    ),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]


urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path("blog/", include("blog.urls")),
    path("", include("core.urls")),
)

if settings.DEBUG:
    from django.views.defaults import page_not_found

    urlpatterns += i18n_patterns(
        path(
            "404/",
            lambda request: page_not_found(request, Exception("Page not found")),
            name="preview_404",
        ),
    )
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
