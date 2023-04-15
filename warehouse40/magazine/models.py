from django.db import models
from enum import Enum


class WarehouseZone(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    LOAD_PRIORITY = [
    ("AA", "AA"),
    ("BB", "BB"),
    ("BB", "CC"),
    ("CC", "DD"),
    ("DD", "EE"),
]

    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.FloatField()
    zone_id = models.ForeignKey(
        WarehouseZone, verbose_name=(""), on_delete=models.CASCADE
    )
    load_priority = models.CharField(
        max_length=2, choices=LOAD_PRIORITY
    )


class Worker(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)


class Order(models.Model):
    buyer = models.CharField(max_length=255)
    date_of_order = models.DateField(null=True)
    estimated_time_seconds = models.PositiveIntegerField(null=True)

    ORDER_STATUS = [("FINISHED", "realized"), ("TO_REALIZE", "to_realize"), ("IN_PROGRESS", "in_progress")]

    order_status = models.CharField(
        max_length=11, choices=ORDER_STATUS
    )
    pick_up_time = models.DateTimeField(null=True)
    worker_id = models.ForeignKey(Worker, verbose_name=(""), on_delete=models.CASCADE)


class ProductOrder(models.Model):
    product_id = models.ForeignKey(Product, verbose_name=(""), on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, verbose_name=(""), on_delete=models.CASCADE)
