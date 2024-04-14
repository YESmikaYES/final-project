from django.urls import path
from . import views

urlpatterns = [
    path("car/<int:id>", views.borrow_car, name="car_borrow")
]