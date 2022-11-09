from django.db import models


class City(models.Model):
    title = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def str(self):
        return self.title