from django import template
from django.utils.safestring import mark_safe
import markdown as md

register = template.Library()

_EXTENSIONS = [
    "extra",
    "sane_lists",
    "toc",
    "nl2br",
]


@register.filter(name="markdownify")
def markdownify(value):
    """Render Markdown text to safe HTML."""
    if not value:
        return ""
    html = md.markdown(str(value), extensions=_EXTENSIONS)
    return mark_safe(html)
