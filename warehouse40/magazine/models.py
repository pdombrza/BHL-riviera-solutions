from django.db import models
from enum import Enum


class WarehouseZone(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    class LoadPriority(Enum):
        A = "AA"
        B = "BB"
        C = "CC"
        D = "DD"

    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.FloatField()
    zone_id = models.ForeignKey(
        WarehouseZone, verbose_name=_(""), on_delete=models.CASCADE
    )
    load_priority = models.CharField(
        max_length=2, choices=LoadPriority, default=LoadPriority.A
    )


class Worker(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)


class Order(models.Model):
    buyer = models.CharField(max_length=255)
    date_of_order = models.DateField(null=True)
    estimated_time = models.TimeField(null=True)


# class ProductOrder(models.Model):
