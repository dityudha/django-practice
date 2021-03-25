from django.contrib import admin

# Register your models here.

from .models import Cars
# from .models import Bike

admin.site.register(Cars)
# admin.site.register(Bike)