from django.contrib import admin

from .models import *


@admin.register(Hacker)
class HackerAdmin(admin.ModelAdmin):

    # list_display = ('id', )
    list_per_page = 30

    fields = ([f.name for f in Hacker._meta.fields][1:])

    # search_fields = ['segment', 'id']
    # list_filter = ('storage', 'mime__type', 'mime')

@admin.register(City)
class City(admin.ModelAdmin):

    fields = ([f.name for f in City._meta.fields][1:])

@admin.register(Organizer)
class Organizer(admin.ModelAdmin):

    fields = ([f.name for f in Organizer._meta.fields][1:])

@admin.register(Hackathon)
class Hacakthon(admin.ModelAdmin):

    fields = ([f.name for f in Hackathon._meta.fields][1:])

@admin.register(Team)
class Team(admin.ModelAdmin):

    fields = ([f.name for f in Team._meta.fields][1:])
