from django.http import HttpResponseRedirect
from user_management.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from social_core.exceptions import AuthException


def get_user(backend, user, response, *args, **kwargs):
    if backend.name == 'google-oauth2' and kwargs:
        email = kwargs['uid']
        S = User.objects.filter(email__contains=email).values().distinct()
        if S:
          return user
        else:
            return redirect('failed2')
