from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter()
def highlight_text(spec_word, value):
    try:
        return mark_safe(str(value).replace(spec_word, f'<a class="bg-warning">{spec_word}</a>'))
    except:
        return value

