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
        if form.data.get("password1") != form.data.get("password2"):
            password_mismatch = True
            name_error = False
        elif form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('car_list')
        else:
            password_mismatch = False
            name_error = True


    else:
        form = SignUpForm()
        password_mismatch = False
        name_error = False

    context = {
        'form': form,
        'pwd_error' : password_mismatch,
        "name_error" : name_error
        }
    template = loader.get_template("signup.html")

    return HttpResponse(template.render(context=context, request=request))

def logout_view(request):
    logout(request)
    return redirect("home_page")

@login_required
def view_profile(request):

    try:
        cars = get_list_or_404(Car, current_user = request.user.profile)

    except:
        context = {'user' : request.user, 'cars_bool': False}
        template = loader.get_template("profile.html")
        return HttpResponse(template.render(context=context, request=request))
    
    else:
        cars = get_list_or_404(Car, current_user = request.user.profile)
        context = {'user' : request.user,
                   'cars_bool': True,
               'cars' : cars}
        template = loader.get_template("profile.html")
        return HttpResponse(template.render(context=context, request=request))
