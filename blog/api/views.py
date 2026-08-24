from rest_framework import viewsets

from blog.models import Post

from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """Private CRUD for blog posts. PUT is disabled; use PATCH for updates."""

    serializer_class = PostSerializer
    lookup_field = "slug"
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]

    def get_queryset(self):
        return (
            Post.objects.select_related("category")
            .prefetch_related("tags")
            .all()
        )
