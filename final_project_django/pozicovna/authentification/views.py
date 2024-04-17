from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.http import HttpResponse
from django.template import loader

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
    context = {'user' : request.user}
    template = loader.get_template("profile.html")

    return HttpResponse(template.render(context=context, request=request))