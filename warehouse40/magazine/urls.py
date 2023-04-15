from django.urls import path
from .views import product_list

<<<<<<< HEAD
urlpatterns = [path("", views.index, name="index"),
               path('load_data/', views.load_data, name="load_data")]
=======
urlpatterns = [
    path('', product_list, name='product_list'),
    # add other URL patterns as needed
]
>>>>>>> f52e9bda3b01bf35ce30d479a2059e4b63fa1d20
