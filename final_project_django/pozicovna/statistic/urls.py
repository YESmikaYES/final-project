from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("cars/", views.load_charts, name="statistics_cars")
]