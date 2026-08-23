def get_client_ip(request):
    """Return the connecting client IP (REMOTE_ADDR only; no X-Forwarded-For trust)."""
    return request.META.get("REMOTE_ADDR")
