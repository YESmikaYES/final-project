from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.http import HttpResponse, Http404
from django.template import loader
from core.models import Car

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('car_list')
    else:
        form = SignUpForm()

    context = {
        'form': form
        }
    template = loader.get_template("signup.html")

    return HttpResponse(template.render(context=context, request=request))

def logout(request):
    logout(request)
    return HttpResponse("logged out")

@login_required
def view_profile(request):

    try:
        cars = get_list_or_404(Car, current_user = request.user.profile)

    except:
        context = {'user' : request.user}
        template = loader.get_template("profile.html")
        return HttpResponse(template.render(context=context, request=request))
    
    else:
        cars = get_list_or_404(Car, current_user = request.user.profile)
        context = {'user' : request.user,
               'cars' : cars}
        template = loader.get_template("profile_with_cars.html")
        return HttpResponse(template.render(context=context, request=request))
