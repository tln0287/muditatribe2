import ast
from django import template
from django.contrib.auth.models import Group
from counsellor.encryption_util import encrypt
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

