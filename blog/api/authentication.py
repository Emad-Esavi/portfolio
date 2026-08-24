import secrets

from django.conf import settings
from rest_framework import authentication, exceptions


class BlogAPIKeyUser:
    """Minimal authenticated principal for the blog automation API key."""

    is_authenticated = True
    pk = None
    id = None

    def __str__(self):
        return "blog-api-key"


class BlogAPIKeyAuthentication(authentication.BaseAuthentication):
    """Authenticate requests with the ``X-API-Key`` header."""

    header_name = "X-API-Key"

    def authenticate(self, request):
        provided = request.headers.get(self.header_name)
        if not provided:
            return None

        expected = getattr(settings, "BLOG_API_KEY", "") or ""
        if not expected:
            raise exceptions.AuthenticationFailed("API key is not configured.")

        if not secrets.compare_digest(provided, expected):
            raise exceptions.AuthenticationFailed("Invalid API key.")

        return (BlogAPIKeyUser(), None)

    def authenticate_header(self, request):
        return self.header_name
