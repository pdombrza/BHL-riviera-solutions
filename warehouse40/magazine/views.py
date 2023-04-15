from django.http import JsonResponse
from .models import Product


def product_list(request):
    products = Product.objects.all()
    products_list = []
    for product in products:
        products_list.append({
            'name': product.name,
            'qyantity': product.quantity,
            'price': product.price,
            'zone_id': product.zone_id,
            'load_priority': product.load_priority
        })
    return JsonResponse(products_list, safe=False)