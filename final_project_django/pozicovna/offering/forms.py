from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import OfferedCar
from django.http import HttpRequest


class CarOfferForm(forms.ModelForm):

    class Meta:
        model = OfferedCar
        fields = ('name', 'wheels', 'car_type', 'manufacturer', 'clutch', 'license_plate', 'kilometrage')
