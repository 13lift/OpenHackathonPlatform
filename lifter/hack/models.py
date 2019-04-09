from uuid import uuid4

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
User = get_user_model()
from django.db import models

from lifter.profiles.models import City

class Hacker(models.Model):
    """
    Участник команды
    """

    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )

    skils = models.CharField(max_length=32)
    rating = models.PositiveIntegerField()
    github = models.URLField()

    slug = models.SlugField(
        max_length=20,
        blank=False,
    )

    def __str__(self):
        return self.slug


class TeamStatus(object):
    """
    Статусы команды
    """
    NOT_READY = 0
    READY = 1
    EXCLUDED = -1

    CHOICES = (
        (NOT_READY, 'Team NOT ready'),
        (READY, 'Team ready!'),
        (EXCLUDED, 'excluded'),
    )


class Team(models.Model):
    """
    Команда хакатона
    """

    members = models.ManyToManyField(Hacker)

    name = models.CharField(max_length=32)
    info = models.CharField(max_length=255)
    github = models.URLField()
    presentation = models.FileField()

    image = models.ImageField()

    leader = models.ForeignKey(
        Hacker,
        on_delete=models.DO_NOTHING,
        related_name='leader'
    )

    status = models.SmallIntegerField(
        db_index=True,
        choices=TeamStatus.CHOICES,
        default=TeamStatus.NOT_READY,
        verbose_name=_('Статус команды')
    )

    # TODO: сделать в процентах
    progress = models.PositiveSmallIntegerField()

    rating = models.PositiveIntegerField()

    slug = models.SlugField(
        max_length=20,
        blank=False,
    )

    def __str__(self):
        return self.slug



class Organizer(models.Model):

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
    description = models.TextField()
    image = models.ImageField()
    url = models.URLField()

    slug = models.SlugField(
        max_length=20,
        blank=False,
    )

    def __str__(self):
        return self.slug


class Sponsor(models.Model):

    name = models.CharField(max_length=32)

    manager = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )

    info = models.CharField(max_length=32)
    description = models.TextField()
    url = models.URLField()
    image = models.ImageField()

    slug = models.SlugField(
        max_length=20,
        blank=False,
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

    sponsor = models.ManyToManyField(Sponsor)
    organizer = models.ForeignKey(Organizer, on_delete=models.DO_NOTHING)

    name = models.CharField(max_length=32)
    url = models.URLField(max_length=150)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()

    address = models.CharField(max_length=32)
    city = models.ForeignKey(
        City,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )

    info = models.CharField(max_length=32)
    program = models.TextField()
    description = models.TextField()
    image = models.ImageField()

    slug = models.SlugField(
        max_length=20,
        blank=False,
    )

    def __str__(self):
        return self.slug


class Nomination(models.Model):
    """
    Призовые номинации
    """

    name = models.CharField(max_length=32)

    sponsor = models.ForeignKey(
        Sponsor,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )

    hackathon = models.ForeignKey(
        Hackathon,
        on_delete=models.DO_NOTHING,
        blank=False,
        null=False,
    )

    teams = models.ManyToManyField(
        Team,
        blank=True,
    )

    info = models.CharField(max_length=32, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    prize = models.PositiveSmallIntegerField(blank=True)

    def __str__(self):
        return self.name
