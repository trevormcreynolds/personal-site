import markdown
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))

@register.filter(name='render_markdown')
@stringfilter
def render_markdown(text):
    md = markdown.Markdown(extensions=["fenced_code", "codehilite"])
    return mark_safe(md.convert(text))