from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateField(blank=True, null=True)
    nationality = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    biography = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
