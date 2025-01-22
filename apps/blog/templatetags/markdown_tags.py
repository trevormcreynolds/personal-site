import markdown
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
@stringfilter
def render_markdown(text):
    md = markdown.Markdown(extensions=["extra", "tables", "fenced_code", "codehilite"])
    return mark_safe(md.convert(text))
