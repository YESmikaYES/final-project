from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("offer/car/", views.send_car_offer, name="offer_car"),
]