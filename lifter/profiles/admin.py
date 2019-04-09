# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Profile._meta.fields]
    list_filter = ('created_at',)
    search_fields = ['id']

    raw_id_fields = ('user',)

# @admin.register(User)
# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = [f.name for f in User._meta.fields]
