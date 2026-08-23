from django.urls import path

from . import views
from .feeds import LatestPostsFeed

app_name = "blog"

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("feed/", LatestPostsFeed(), name="feed"),
    path("category/<slug:slug>/", views.category_posts, name="category_posts"),
    path("tag/<slug:slug>/", views.tag_posts, name="tag_posts"),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
]
