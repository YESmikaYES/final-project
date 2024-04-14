from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.http import HttpResponse



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    borrowed_vehicles = models.IntegerField(verbose_name="number of vehicles borrowed by user", validators=[MaxValueValidator(5), MinValueValidator(0)], default=0)
    def __str__(self) -> str:
        return self.user.username

class Car(models.Model):
    name = models.CharField(max_length=50)
    wheels = models.IntegerField()
    car_type = models.CharField(max_length=20)
    manufacturer = models.CharField(max_length=50)
    clutch = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=10)
    kilometrage = models.IntegerField()
    current_user = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="name of current user of this car", blank=True, default=None, null=True)
    
    def borrow(self, user:Profile):
        if user.profile.borrowed_vehicles < 5 and self.current_user == None:
            self.current_user = user.profile
            user.profile.borrowed_vehicles += 1
            self.save()
            user.profile.save()

        else:
            return HttpResponse("User has reached borrowed vehicle limit")


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