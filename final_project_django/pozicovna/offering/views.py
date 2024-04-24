from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.contrib.auth import logout
from .models import OfferedCar
from .forms import CarOfferForm
from django.template import loader
from django.contrib.auth.models import User



# Create your views here.
@login_required(login_url='login')
def send_car_offer(request):
    if request.method == "POST":
        form = CarOfferForm(request.POST)
        if form.is_valid():
            form.instance.offering_user = request.user.profile
            form.save()
            return redirect("car_list")
    else:
        form = CarOfferForm()

    context = {"form": form}
    template = loader.get_template("offer_car.html")
    return HttpResponse(template.render(context=context, request=request))

@login_required(login_url='login')
@permission_required("core.add_car")        
def all_offered_cars(request):
    offers = OfferedCar.objects.all()
    context = {
        "offers": offers
        }
    
    template = loader.get_template("offered_cars.html")
    return HttpResponse(template.render(context=context, request=request))

@login_required(login_url='login')
@permission_required("core.add_car")        
def accept_car_offer(request,id):
    car = OfferedCar.objects.get(id=id)
    car.accept_car()
    return redirect("all_offers")