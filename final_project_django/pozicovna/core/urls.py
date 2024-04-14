from django.urls import path
from . import views

urlpatterns = [
    path("cars", views.car_list, name="car_list"),
    # path("motorcycles", views.motorcycle_list, name="motorcycle_list"),
    path("cars/<int:id>", views.car_details, name="car_detail"),
    path("li", views.index1, name="li"),
    path("lo", views.index2,  name="lo"),
]