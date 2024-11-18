import ast
from django import template
from django.contrib.auth.models import Group
from web.encryption_util import encrypt
from user_management.models import UserSupport

register = template.Library()
from django.utils.safestring import mark_safe


@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()


@register.filter(name='encrypting')
def encrypting(id):
    encrypt_id = encrypt(id)
    return encrypt_id


@register.filter(name='to_int')
def to_int(value):
    try:
        return int(float(value))
    except:
        return value

@register.filter(name='next_page')
def next_page(page):
    try:
        page = int(page) + 1
        p = encrypt(str(page))
        return p
    except:
        return page


@register.filter(name='previous_page')
def previous_page(page):
    try:
        print("page-----")
        print(page)
        print("page----")
        if page == "1":
            return encrypt(page)
        else:
            page = int(page) - 1
            p = encrypt(str(page))
            return p
    except:
        return page



@register.simple_tag
def get_support_count(user):

    if user.groups.filter(name="Admin").exists():
        data = UserSupport.objects.all().values()
    else:
        data = UserSupport.objects.filter(user__u_id=user.u_id).values()
    return len(data) if data else 0
