from django.db import models
from django.utils.text import slugify

from shared.models import BaseTimestampModel


class Team(BaseTimestampModel):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="team/logo/", null=True, blank=True)
    club = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Team, self).save(*args, **kwargs)
