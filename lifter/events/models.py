from uuid import uuid4

from django.contrib.auth import get_user_model
User = get_user_model()

from django.db import models

from lifter.hack.models import City, Organizer


class EventType(models.Model):

    name = models.CharField(max_length=32)
    info = models.CharField(max_length=32)

    slug = models.SlugField(
        max_length=20,
        blank=True,
    )

    def __str__(self):
        return self.slug


class Event(models.Model):

    name = models.CharField(max_length=32)
    city = models.ForeignKey(
        City,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    type = models.ForeignKey(
        EventType,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    organizer = models.ForeignKey(
        Organizer,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )

    info = models.CharField(max_length=32)

    slug = models.SlugField(
        max_length=20,
        blank=True,
    )

    def __str__(self):
        return self.slug
