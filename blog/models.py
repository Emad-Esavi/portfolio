from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.html import strip_tags
from django.utils.text import Truncator


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("blog:category_posts", args=[self.slug])


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("blog:tag_posts", args=[self.slug])


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        PUBLISHED = "published", "Published"

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    excerpt = models.TextField(
        blank=True,
        help_text="Optional short summary. If empty, one is generated from the content.",
    )
    content = models.TextField(
        help_text="Post body written in Markdown.",
    )

    featured_image = models.ImageField(
        upload_to="blog/",
        blank=True,
        null=True,
        help_text="Local upload. Takes precedence over the external URL.",
    )
    featured_image_url = models.URLField(
        blank=True,
        help_text="External image URL (useful for n8n / hosted images).",
    )
    featured_image_alt = models.CharField(
        max_length=200,
        blank=True,
        help_text="Alt text for the featured image (SEO / accessibility).",
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="posts",
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name="posts",
    )

    author_name = models.CharField(
        max_length=150,
        blank=True,
        help_text="Plain-text author. Leave blank to use the site profile name.",
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT,
        db_index=True,
    )
    is_featured = models.BooleanField(default=False)
    published_at = models.DateTimeField(
        blank=True,
        null=True,
        help_text="Set automatically on first publish; editable for backdating.",
    )

    seo_title = models.CharField(
        max_length=70,
        blank=True,
        help_text="Optional override for the <title> tag (max ~70 chars).",
    )
    seo_description = models.CharField(
        max_length=160,
        blank=True,
        help_text="Optional meta description (max ~160 chars).",
    )

    view_count = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-published_at", "-created_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.status == self.Status.PUBLISHED and self.published_at is None:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.slug])

    @property
    def is_published(self):
        return self.status == self.Status.PUBLISHED

    @property
    def image_url(self):
        """Prefer local upload; fall back to external URL."""
        if self.featured_image:
            return self.featured_image.url
        return self.featured_image_url or ""

    @property
    def reading_time(self):
        """Approximate reading time in minutes (200 wpm)."""
        words = len(self.content.split())
        return max(1, round(words / 200))

    @property
    def plain_excerpt(self):
        if self.excerpt:
            return self.excerpt
        plain = strip_tags(self.content)
        return Truncator(plain).chars(160)

    @classmethod
    def published(cls):
        return cls.objects.filter(status=cls.Status.PUBLISHED)
