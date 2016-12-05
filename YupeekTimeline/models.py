from django.db import models
from django.utils import timezone


class Element(models.Model):

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

    PROD = 'Prod'
    STAGING = 'Staging'

    TYPE_CHOICES = (
        (PROD, 'Prod'),
        (STAGING, 'Staging'),

    )

    type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        default=None,
        null=True,
        blank=True
    )

    def __str__(self):
        return "{} - {}".format(self.content, self.type)
