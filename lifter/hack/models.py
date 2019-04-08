from uuid import uuid4

from django.contrib.auth import get_user_model
User = get_user_model()
from django.db import models


class City(models.Model):

    name = models.CharField(max_length=32)
    info = models.CharField(max_length=255)

    slug = models.SlugField(
        max_length=20,
        blank=True,
    )

    def __str__(self):
        return self.slug


class Hacker(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    city = models.ForeignKey(
        City,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    skils = models.CharField(max_length=32)
    rating = models.PositiveIntegerField()

    slug = models.SlugField(
        max_length=20,
        blank=True,
    )

    def __str__(self):
        return self.slug

class Hackathon(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=32)
    city = models.ForeignKey(
        City,
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

class Orginizer(models.Model):

    name = models.CharField(max_length=32)

    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    city = models.ForeignKey(
        City,
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
