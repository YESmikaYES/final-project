from django.urls import path
from . import views

urlpatterns = [
    path("car/<int:id>", views.return_car, name="car_return")
]