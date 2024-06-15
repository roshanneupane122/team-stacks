from django import forms
from .models import Hotel, Vehicle

class CombinedForm(forms.Form):
    hotel_name = forms.CharField(max_length=255, label='Hotel Name')
    hotel_address = forms.CharField(widget=forms.Textarea, label='Hotel Address')
    hotel_contact_number = forms.CharField(max_length=15, label='Hotel Contact Number')
    hotel_photo = forms.ImageField(label='Hotel Photo')
    
    vehicle_name = forms.CharField(max_length=255, label='Vehicle Name')
    vehicle_address = forms.CharField(widget=forms.Textarea, label='Vehicle Address')
    vehicle_contact_number = forms.CharField(max_length=15, label='Vehicle Contact Number')
    vehicle_photo = forms.ImageField(label='Vehicle Photo')

