from django.shortcuts import render
from .models import Flight, Passenger
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    passengers = flight.passengers.all()
    non_passengers = Passenger.objects.exclude(flights=flight).all()
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": passengers,
        "non_passengers": non_passengers
    })

def book(request, flight_id):

    if request.method == "POST":   # For a post request, add a new flight
        flight = Flight.objects.get(id=flight_id)   # Accessing the flight
        passenger_id = int(request.POST["passenger"])   # Finding the passenger id from the submitted form data
        passenger = Passenger.objects.get(id=passenger_id)   # Finding the passenger based on the id
        passenger.flights.add(flight)   # Add passenger to the flight      
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))   # Redirect user to flight page