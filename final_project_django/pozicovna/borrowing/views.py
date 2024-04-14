from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import logout

# Create your views here.
@login_required
def borrow_car(request, id):
    return HttpResponse("car borrowed successfully")
