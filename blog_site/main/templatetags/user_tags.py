from django import template
from user.models import *



register = template.Library()


@register.simple_tag()
def get_user():
    return CustomUser.objects.get(first_name='Егор')


@register.simple_tag()
def get_education():
    return Education.objects.filter(custom_user_id=1)


@register.simple_tag()
def get_work_experiance():
    return WorkExperiance.objects.filter(custom_user_id=1)

