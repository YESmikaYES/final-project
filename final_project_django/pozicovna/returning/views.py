from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import logout
from core.models import Car


# Create your views here.
@login_required(login_url='login')
def return_car(request, id):
    car = Car.objects.get(id=id)
    return car.give_back(request.user)