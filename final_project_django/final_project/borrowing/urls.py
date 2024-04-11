from django.urls import path
from . import views

urlpatterns = [
    path("cars", views.car_list, name="car_list"),
    path("motorcycles", views.motorcycle_list, name="motorcycle_list")
]