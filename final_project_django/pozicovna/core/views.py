from django.shortcuts import render
from django.http import HttpResponse
from .models import Car
from django.template import loader
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def car_list(request):
    template = loader.get_template("all_cars.html")
    context = {
        "cars" : Car.objects.all().values()
        }
    

    return HttpResponse(template.render(context=context, request=request))

def car_details(request, id):
    template = loader.get_template("detail_car.html")
    context = {
        "car" : Car.objects.get(id=id)
    }
    return HttpResponse(template.render(context=context, request=request))

def index1(request):
    user = authenticate(request=request, username="test4", password="Slniecko04")
    login(request=request, user=user)
    return HttpResponse("logged in as test4")

def index2(request):
    logout(request)
    return HttpResponse("logged out")

# def motorcycle_list(request):
#     return HttpResponse("list of all motorcycles")
