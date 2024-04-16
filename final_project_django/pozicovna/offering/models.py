from django.db import models
from core.models import Profile, Car

# Create your models here.

# Create your models here.
class OfferedCar(models.Model):
    name = models.CharField(max_length=50)
    wheels = models.IntegerField()
    car_type = models.CharField(max_length=20)
    manufacturer = models.CharField(max_length=50)
    clutch = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=10)
    kilometrage = models.IntegerField()
    offering_user = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="name of current user of this car")

    def accept_car(self):
        pass