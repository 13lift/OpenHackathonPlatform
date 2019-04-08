from django.contrib import admin

from .models import *


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    fields = ([f.name for f in Event._meta.fields][1:])

@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):

    fields = ([f.name for f in EventType._meta.fields][1:])
