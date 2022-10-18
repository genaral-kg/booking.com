from django.db import models

from django.utils.text import slugify


class City(models.Model):     #slug of category
    name = models.CharField(max_length=30,unique=True)              #name of category

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name
