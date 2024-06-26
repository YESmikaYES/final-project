from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="login.html", next_page="profile"), name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout_view, name="logout"),
    path("", views.view_profile, name="profile")
]