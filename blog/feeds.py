from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.utils.feedgenerator import Rss201rev2Feed
from django.utils.translation import gettext_lazy as _

from .models import Post


class LatestPostsFeed(Feed):
    title = _("Portfolio Blog")
    description = _("Latest articles and notes from the portfolio blog.")
    feed_type = Rss201rev2Feed

    def link(self):
        return reverse("blog:post_list")

    def items(self):
        return (
            Post.published()
            .select_related("category")
            .prefetch_related("tags")
            .order_by("-published_at")[:20]
        )

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.plain_excerpt

    def item_link(self, item):
        return item.get_absolute_url()

    def item_pubdate(self, item):
        return item.published_at

    def item_updateddate(self, item):
        return item.updated_at

    def item_author_name(self, item):
        return item.author_name or None

    def item_categories(self, item):
        cats = []
        if item.category:
            cats.append(item.category.name)
        cats.extend(tag.name for tag in item.tags.all())
        return cats
