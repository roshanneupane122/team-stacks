from django.db import models

# Create your models here.
from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='hotel_photos/')

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='vehicle_photos/')

    def __str__(self):
        return self.name
    
from django.db import models

class Booking(models.Model):
    package_title = models.CharField(max_length=200)
    total_cost = models.DecimalField(max_digits=8, decimal_places=2)
    # Add more fields as needed to capture other relevant information

    def __str__(self):
        return self.package_title
