import json
import re

from django.core.validators import URLValidator
from django.utils.text import slugify
from rest_framework import serializers

from blog.models import Category, Post, Tag

_WHITESPACE_RE = re.compile(r"\s+")


def normalize_label(value: str) -> str:
    """Strip and collapse internal whitespace; reject empty results."""
    cleaned = _WHITESPACE_RE.sub(" ", (value or "").strip())
    if not cleaned:
        raise serializers.ValidationError("This field may not be blank.")
    return cleaned


def get_or_create_category(name: str) -> Category:
    cleaned = normalize_label(name)
    slug = slugify(cleaned)
    if not slug:
        raise serializers.ValidationError(
            "Category name must produce a valid slug."
        )
    category, _ = Category.objects.get_or_create(
        slug=slug,
        defaults={"name": cleaned},
    )
    return category


def get_or_create_tag(name: str) -> Tag:
    cleaned = normalize_label(name)
    slug = slugify(cleaned)
    if not slug:
        raise serializers.ValidationError("Tag name must produce a valid slug.")
    tag, _ = Tag.objects.get_or_create(
        slug=slug,
        defaults={"name": cleaned},
    )
    return tag


SLUG_MAX_LENGTH = 50


def clip_slug(value: str) -> str:
    slug = slugify(value) or "post"
    slug = slug[:SLUG_MAX_LENGTH].rstrip("-")
    return slug or "post"


def unique_slug_from_title(title: str, exclude_pk=None) -> str:
    base = clip_slug(title)
    slug = base
    counter = 2
    qs = Post.objects.all()
    if exclude_pk is not None:
        qs = qs.exclude(pk=exclude_pk)
    while qs.filter(slug=slug).exists():
        suffix = f"-{counter}"
        slug = f"{base[: SLUG_MAX_LENGTH - len(suffix)]}{suffix}".rstrip("-")
        if not slug:
            slug = f"post{suffix}"[:SLUG_MAX_LENGTH]
        counter += 1
    return slug


class PostSerializer(serializers.ModelSerializer):
    category = serializers.CharField(
        required=False,
        allow_null=True,
        allow_blank=True,
        write_only=True,
    )
    tags = serializers.ListField(
        child=serializers.CharField(),
        required=False,
        allow_empty=True,
        write_only=True,
    )
    featured_image = serializers.ImageField(
        required=False,
        allow_null=True,
    )
    featured_image_url = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=200,
    )
    image_url = serializers.CharField(read_only=True)
    url = serializers.SerializerMethodField()

    title_fa = serializers.CharField(required=False, allow_blank=True, max_length=200)
    excerpt_fa = serializers.CharField(required=False, allow_blank=True)
    content_fa = serializers.CharField(required=False, allow_blank=True)
    featured_image_alt_fa = serializers.CharField(
        required=False, allow_blank=True, max_length=200
    )
    seo_title_fa = serializers.CharField(required=False, allow_blank=True, max_length=70)
    seo_description_fa = serializers.CharField(
        required=False, allow_blank=True, max_length=160
    )

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "title_fa",
            "slug",
            "excerpt",
            "excerpt_fa",
            "content",
            "content_fa",
            "featured_image",
            "featured_image_url",
            "featured_image_alt",
            "featured_image_alt_fa",
            "image_url",
            "category",
            "tags",
            "author_name",
            "status",
            "is_featured",
            "published_at",
            "seo_title",
            "seo_title_fa",
            "seo_description",
            "seo_description_fa",
            "view_count",
            "url",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "published_at",
            "view_count",
            "image_url",
            "url",
            "created_at",
            "updated_at",
        ]
        extra_kwargs = {
            "slug": {"required": False, "allow_blank": True, "max_length": 50},
            "title": {"required": True},
            "content": {"required": True},
            "status": {"required": False},
        }

    def get_url(self, obj):
        return obj.get_absolute_url()

    def to_internal_value(self, data):
        if hasattr(data, "copy"):
            data = data.copy()
        tags = data.get("tags")
        if isinstance(tags, str):
            raw = tags.strip()
            if not raw:
                parsed = []
            elif raw.startswith("["):
                try:
                    parsed = json.loads(raw)
                except json.JSONDecodeError as exc:
                    raise serializers.ValidationError(
                        {"tags": "Enter a JSON array of tag names."}
                    ) from exc
                if not isinstance(parsed, list):
                    raise serializers.ValidationError(
                        {"tags": "Enter a JSON array of tag names."}
                    )
            else:
                parsed = [part.strip() for part in raw.split(",") if part.strip()]
            parsed = [str(item) for item in parsed]
            if hasattr(data, "setlist"):
                data.setlist("tags", parsed)
            else:
                data["tags"] = parsed
        return super().to_internal_value(data)

    def validate_featured_image_url(self, value):
        if value in (None, ""):
            return ""
        validator = URLValidator(schemes=["http", "https"])
        try:
            validator(value)
        except Exception as exc:
            raise serializers.ValidationError(
                "Enter a valid HTTP or HTTPS URL."
            ) from exc
        return value

    def validate_category(self, value):
        if value in (None, ""):
            return None
        return normalize_label(value)

    def validate_tags(self, value):
        if not value:
            return []
        seen_slugs = set()
        cleaned = []
        for item in value:
            label = normalize_label(item)
            slug = slugify(label)
            if not slug:
                raise serializers.ValidationError(
                    "Tag name must produce a valid slug."
                )
            if slug in seen_slugs:
                continue
            seen_slugs.add(slug)
            cleaned.append(label)
        return cleaned

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["category"] = instance.category.name if instance.category else None
        data["tags"] = list(instance.tags.values_list("name", flat=True))
        return data

    def _resolve_category(self, category_name):
        if category_name is None:
            return None
        return get_or_create_category(category_name)

    def _apply_tags(self, post, tag_names):
        tags = [get_or_create_tag(name) for name in tag_names]
        post.tags.set(tags)

    def create(self, validated_data):
        category_name = validated_data.pop("category", serializers.empty)
        tag_names = validated_data.pop("tags", serializers.empty)

        if not validated_data.get("slug"):
            validated_data["slug"] = unique_slug_from_title(
                validated_data.get("title", "")
            )
        else:
            validated_data["slug"] = unique_slug_from_title(
                validated_data["slug"]
            )

        if category_name is not serializers.empty:
            validated_data["category"] = self._resolve_category(category_name)

        post = Post.objects.create(**validated_data)

        if tag_names is not serializers.empty:
            self._apply_tags(post, tag_names)

        return post

    def update(self, instance, validated_data):
        category_name = validated_data.pop("category", serializers.empty)
        tag_names = validated_data.pop("tags", serializers.empty)

        if "slug" in validated_data and not validated_data["slug"]:
            validated_data.pop("slug")

        if category_name is not serializers.empty:
            instance.category = self._resolve_category(category_name)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if tag_names is not serializers.empty:
            self._apply_tags(instance, tag_names)

        return instance
