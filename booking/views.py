from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import CombinedForm
from .models import Hotel, Vehicle

def combined_create_view(request):
    if request.method == 'POST':
        form = CombinedForm(request.POST, request.FILES)
        if form.is_valid():
            # Save hotel data
            hotel = Hotel(
                name=form.cleaned_data['hotel_name'],
                address=form.cleaned_data['hotel_address'],
                contact_number=form.cleaned_data['hotel_contact_number'],
                photo=form.cleaned_data['hotel_photo']
            )
            hotel.save()
            
            # Save vehicle data
            vehicle = Vehicle(
                name=form.cleaned_data['vehicle_name'],
                address=form.cleaned_data['vehicle_address'],
                contact_number=form.cleaned_data['vehicle_contact_number'],
                photo=form.cleaned_data['vehicle_photo']
            )
            vehicle.save()
            
            return redirect('success_page')  # Redirect to a success page or any other page you want
    else:
        form = CombinedForm()
    return render(request, 'combined_form.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')

def book(request):
    return render(request, 'booking_form.html')


from django.shortcuts import render
from .models import Hotel, Vehicle

def display_cards_view(request):
    hotels = Hotel.objects.all()
    vehicles = Vehicle.objects.all()
    context = {
        'hotels': hotels,
        'vehicles': vehicles,
    }
    return render(request, 'display_cards.html', context)


# views.py (inside your Django app)
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Booking
import json

@csrf_exempt
def save_booking(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        package_title = data.get('package_title')
        total_cost = data.get('total_cost')

        # Save to database
        booking = Booking(package_title=package_title, total_cost=total_cost)
        booking.save()

        return JsonResponse({'message': 'Booking saved successfully!'}, status=201)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)