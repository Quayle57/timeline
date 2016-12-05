from django.db import models
from django.utils import timezone


class Timeline(models.Model):

    title = models.CharField(
        max_length=255,
        blank=False
    )

    def __str__(self):
        return self.title


class Element(models.Model):

    title = models.CharField(
        max_length=255
    )

    content = models.CharField(
        max_length=2048,
        blank=False,
        default=None
    )

    updated_date = models.DateTimeField(
        auto_now=True,
        blank=False
    )

    created_date = models.DateTimeField(
        default=timezone.now,
        blank=False
    )

    start_date = models.DateTimeField(
        blank=False,
        null=True
    )

    end_date = models.DateTimeField(
        blank=True,
        null=True
    )

    timeline = models.ForeignKey(
        'Timeline',
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return "{} - {}".format(self.title, self.timeline)
