from django.db import models

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=50)
    wheels = models.IntegerField()
    car_type = models.CharField(max_length=20)
    manufacturer = models.CharField(max_length=50)
    clutch = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=10)
    kilometrage = models.IntegerField()


class Motorcycle(models.Model):
    # to be added
    pass

    # name = models.CharField(max_length=50)
    # wheels = models.IntegerField()
    # motorcycle_type = models.CharField(max_length=20)
    # manufacturer = models.CharField(max_length=50)
    # clutch = models.CharField(max_length=50)
    # license_plate = models.CharField(max_length=10)
    # kilometrage = models.IntegerField()