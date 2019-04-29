from django import template
from ..models import *

register = template.Library()


@register.simple_tag
def get_pictures():
    return Picture.objects.all()


@register.simple_tag
def get_articles():
    return Message.objects.all()

