from rest_framework import serializers

from .models import Cars
from .models import Bike

class CarsSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cars
        fields = ('id','name', 'brand')

class BikeSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bike
        fields = ('id','name', 'brand')