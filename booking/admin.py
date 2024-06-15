from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Hotel, Vehicle

class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'contact_number', 'photo')

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'contact_number', 'photo')

admin.site.register(Hotel, HotelAdmin)
admin.site.register(Vehicle, VehicleAdmin)

from django.contrib import admin
from .models import Booking

admin.site.register(Booking)