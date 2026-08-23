"""Seed the blog with categories, tags, and published posts (EN + FA).

Usage:
    python manage.py seed_blog
    python manage.py seed_blog --clear
"""

from datetime import timedelta

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
from django.utils.text import slugify

from blog.models import Category, Post, Tag
from blog.seed_data import CATEGORIES, POSTS, TAGS


class Command(BaseCommand):
    help = (
        "Seed blog categories, tags, and at least five published posts "
        "with English and Persian translations."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear",
            action="store_true",
            help=(
                "Delete existing posts/tags/categories that match seed slugs "
                "before inserting."
            ),
        )

    @transaction.atomic
    def handle(self, *args, **options):
        if options["clear"]:
            self._clear_seeded()

        categories = self._seed_categories()
        tags = self._seed_tags()
        created, updated = self._seed_posts(categories, tags)

        self.stdout.write(
            self.style.SUCCESS(
                f"Blog seed complete: {len(categories)} categories, "
                f"{len(tags)} tags, {created} posts created, "
                f"{updated} posts updated."
            )
        )

    def _clear_seeded(self):
        post_slugs = [p["slug"] for p in POSTS]
        tag_slugs = [t["slug"] for t in TAGS]
        category_slugs = [c["slug"] for c in CATEGORIES]

        deleted_posts, _ = Post.objects.filter(slug__in=post_slugs).delete()
        deleted_tags, _ = Tag.objects.filter(slug__in=tag_slugs).delete()
        deleted_cats, _ = Category.objects.filter(slug__in=category_slugs).delete()

        self.stdout.write(
            self.style.WARNING(
                f"Cleared seed data: {deleted_posts} posts, "
                f"{deleted_tags} tags, {deleted_cats} categories."
            )
        )

    def _seed_categories(self):
        by_slug = {}
        for item in CATEGORIES:
            category, created = Category.objects.update_or_create(
                slug=item["slug"],
                defaults={
                    "name_en": item["name_en"],
                    "name_fa": item["name_fa"],
                    "description_en": item["description_en"],
                    "description_fa": item["description_fa"],
                },
            )
            by_slug[item["slug"]] = category
            verb = "Created" if created else "Updated"
            self.stdout.write(f"  {verb} category: {category.slug}")
        return by_slug

    def _seed_tags(self):
        by_slug = {}
        for item in TAGS:
            tag, created = Tag.objects.update_or_create(
                slug=item["slug"],
                defaults={
                    "name_en": item["name_en"],
                    "name_fa": item["name_fa"],
                },
            )
            by_slug[item["slug"]] = tag
            verb = "Created" if created else "Updated"
            self.stdout.write(f"  {verb} tag: {tag.slug}")
        return by_slug

    def _seed_posts(self, categories, tags):
        created_count = 0
        updated_count = 0
        now = timezone.now()

        for item in POSTS:
            slug = item["slug"] or slugify(item["title_en"])[:50]
            published_at = now - timedelta(days=item["published_days_ago"])

            defaults = {
                "title_en": item["title_en"],
                "title_fa": item["title_fa"],
                "excerpt_en": item["excerpt_en"],
                "excerpt_fa": item["excerpt_fa"],
                "content_en": item["content_en"].strip(),
                "content_fa": item["content_fa"].strip(),
                "featured_image_url": item["featured_image_url"],
                "featured_image_alt_en": item["featured_image_alt_en"],
                "featured_image_alt_fa": item["featured_image_alt_fa"],
                "seo_title_en": item["seo_title_en"],
                "seo_title_fa": item["seo_title_fa"],
                "seo_description_en": item["seo_description_en"],
                "seo_description_fa": item["seo_description_fa"],
                "category": categories[item["category"]],
                "author_name": item.get("author_name", ""),
                "status": Post.Status.PUBLISHED,
                "is_featured": item.get("is_featured", False),
                "published_at": published_at,
            }

            post, created = Post.objects.update_or_create(
                slug=slug,
                defaults=defaults,
            )
            post.tags.set([tags[tag_slug] for tag_slug in item["tags"]])

            if created:
                created_count += 1
                verb = "Created"
            else:
                updated_count += 1
                verb = "Updated"
            self.stdout.write(f"  {verb} post: {post.slug}")

        return created_count, updated_count
