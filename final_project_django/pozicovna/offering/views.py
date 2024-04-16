from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import logout
from core.models import Car
from .forms import CarOfferForm
from django.template import loader


# Create your views here.
@login_required
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
        