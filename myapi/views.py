# from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .serializers import CarsSerializers
from .serializers import BikeSerializers
from .models import Cars
from .models import Bike


class CarsViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all().order_by('name')
    serializer_class = CarsSerializers

class BikeViewSet(viewsets.ModelViewSet):
    queryset = Bike.objects.all().order_by('name')
    serializer_class = BikeSerializers