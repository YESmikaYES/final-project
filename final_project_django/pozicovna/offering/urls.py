from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("offer/car/", views.send_car_offer, name="offer_car"),
    path("all/cars", views.all_offered_cars, name="all_offers"),
    path("all/cars/accept/<int:id>", views.accept_car_offer, name="accept_car")
]