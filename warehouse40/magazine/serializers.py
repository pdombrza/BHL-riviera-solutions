from rest_framework import serializers
from .models import Product, Worker, Order, WarehouseZone


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "quantity",
            "price",
            "zonde_id",
            "load_priority",
        )


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = (
            "id",
            "name",
            "surname",
            "phone_number",
        )


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "id",
            "buyer",
            "date_of_order",
            "estimated_time_seconds",
            "order_status",
            "pick_up_time",
            "worker_id",
        )


class WarehouseZoneSerializers(serializers.ModelSerializer):
    class Meta:
        model = WarehouseZone
        fields = (
            "id",
            "name",
        )
