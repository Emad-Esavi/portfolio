from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from rest_framework.throttling import SimpleRateThrottle


class _SettingsRateThrottle(SimpleRateThrottle):
    """SimpleRateThrottle that reads rates from Django settings at request time."""

    def get_rate(self):
        try:
            return settings.REST_FRAMEWORK["DEFAULT_THROTTLE_RATES"][self.scope]
        except KeyError as exc:
            raise ImproperlyConfigured(
                f"No default throttle rate set for {self.scope!r} scope"
            ) from exc

    def allow_request(self, request, view):
        self.rate = self.get_rate()
        self.num_requests, self.duration = self.parse_rate(self.rate)
        return super().allow_request(request, view)


class BlogAPIWriteThrottle(_SettingsRateThrottle):
    """Rate-limit authenticated POST/PATCH/DELETE on the blog API."""

    scope = "blog_api_write"

    def allow_request(self, request, view):
        if request.method not in ("POST", "PATCH", "DELETE"):
            return True
        if not getattr(request.user, "is_authenticated", False):
            return True
        return super().allow_request(request, view)

    def get_cache_key(self, request, view):
        return self.cache_format % {
            "scope": self.scope,
            "ident": self.get_ident(request),
        }


class BlogAPIReadThrottle(_SettingsRateThrottle):
    """Rate-limit authenticated GET on the blog API."""

    scope = "blog_api_read"

    def allow_request(self, request, view):
        if request.method != "GET":
            return True
        if not getattr(request.user, "is_authenticated", False):
            return True
        return super().allow_request(request, view)

    def get_cache_key(self, request, view):
        return self.cache_format % {
            "scope": self.scope,
            "ident": self.get_ident(request),
        }
