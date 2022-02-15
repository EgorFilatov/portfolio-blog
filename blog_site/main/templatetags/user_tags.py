from django import template
from user.models import *


register = template.Library()


@register.simple_tag()
def get_categories():
    return CustomUser.objects.all()