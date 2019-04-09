from django.db import models

from datetime import timedelta
from django.contrib.auth import get_user_model
User = get_user_model()

BOOLEAN_YN = (
(True, u'Male'),
(False, u'Famale'),
)

class City(models.Model):

    name = models.CharField(max_length=32)
    info = models.CharField(max_length=255)

    slug = models.SlugField(
        max_length=20,
        blank=False,
    )

    # region = models.CharField(max_length=255, blank=True, null=True)
    # country = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.slug


class Profile(models.Model):

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile'
    )

    bio = models.TextField(blank=True)

    image = models.URLField(blank=True, null=True)
    avatar = models.URLField(blank=True, null=True)

    city = models.ForeignKey(
        City,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        related_name='profile'
    )

    gender = models.NullBooleanField(blank=True, null=True, choices=BOOLEAN_YN)
    birthday = models.PositiveSmallIntegerField(blank=True, null=True)
    birthmonth = models.PositiveSmallIntegerField(blank=True, null=True)
    birthyear = models.PositiveSmallIntegerField(blank=True, null=True)

    karma = models.PositiveSmallIntegerField(default=0, null=True)
    login_count = models.PositiveSmallIntegerField(default=0, null=True)
    locale = models.CharField(max_length=255, blank=True, null=True)

    ip = models.CharField(max_length=50, blank=True, null=True)
    # ip = models.GenericIPAddressField(null=True)

    website = models.URLField(blank=True)
    social = models.URLField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


    def get_field(self):
        return [(field.name, field.value_to_string(self)) for field in Profile._meta.fields]

    def __str__(self):
        return self.user.slug

    class Meta:
        db_table = 'profiles'
