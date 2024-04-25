from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader




# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    borrowed_vehicles = models.IntegerField(verbose_name="number of vehicles borrowed by user", validators=[MaxValueValidator(5), MinValueValidator(0)], default=0)
    def __str__(self) -> str:
        return self.user.username
    
    def is_moderator(self):
        if self.user.has_perm("core.add_car"):
            return True
        else:
            return False
    

class Car(models.Model):
    name = models.CharField(max_length=50)
    wheels = models.IntegerField()
    car_type = models.CharField(max_length=20)
    manufacturer = models.CharField(max_length=50)
    clutch = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=10)
    kilometrage = models.IntegerField()
    current_user = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="name of current user of this car", blank=True, default=None, null=True)
    
    def is_borrowed(self):
        if self.current_user == None:
            return False
        else:
            return True

    def borrow(self, user:Profile):
        if not self.is_borrowed():
            if user.profile.borrowed_vehicles < 5:
                self.current_user = user.profile
                user.profile.borrowed_vehicles += 1
                self.save()
                user.profile.save()
                return redirect("profile")
            
            else:
                template = loader.get_template("vehicle_limit.html")
                return HttpResponse(template.render())

        elif self.current_user == user.profile:
            template = loader.get_template("your_vehicle.html")
            return HttpResponse(template.render())
        
        else:
            template = loader.get_template("other_user.html")
            return HttpResponse(template.render())

    def give_back(self, user:Profile) -> HttpResponse:
        if self.current_user == user.profile:
            self.current_user = None
            user.profile.borrowed_vehicles -= 1
            self.save()
            user.profile.save()
            return redirect("profile")
        
        else:
            template = loader.get_template("return_fail.html")
            return HttpResponse(template.render())

    def __str__(self) -> str:
        if self.car_type == "formula":
            return self.name
        else:
            return f"{self.manufacturer} {self.name}"
        



# class Motorcycle(models.Model):
#     # to be added
#     pass

    # name = models.CharField(max_length=50)
    # wheels = models.IntegerField()
    # motorcycle_type = models.CharField(max_length=20)
    # manufacturer = models.CharField(max_length=50)
    # clutch = models.CharField(max_length=50)
    # license_plate = models.CharField(max_length=10)
    # kilometrage = models.IntegerField()