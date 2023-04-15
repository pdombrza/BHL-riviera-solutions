from django.db import models
from enum import Enum


class Product(models.Model):

    class LoadPriority(Enum):
        A = 'AA'
        B = 'BB'
        C = 'CC'
        D = 'DD'

    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.FloatField()
    zone_id = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
    load_priority =models.CharField(max_length=2, choices=LoadPriority, default=LoadPriority.A)
