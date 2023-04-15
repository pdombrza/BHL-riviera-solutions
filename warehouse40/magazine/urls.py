from django.urls import path
from .views import product_list, load_data, index

urlpatterns = [path("", index, name="index"),
               path('load_data/', load_data, name="load_data"),
               path('', product_list, name='product_list'),]
