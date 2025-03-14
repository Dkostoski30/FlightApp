from django.shortcuts import render, redirect

from flight.forms import FlightForm
from flight.models import Flight


# Create your views here.

def index(request):
    return render(request, 'index.html')


def flights(request):
    user_flights = Flight.objects.filter(created_by=request.user, departure_airport="Скопје")
    if request.method == "POST":
        form = FlightForm(request.POST)
        if form.is_valid():
            new_flight = form.save(commit=False)
            new_flight.created_by = request.user
            new_flight.save()
            return redirect('flights')
    else:
        form = FlightForm()

    return render(request, 'flights.html', {'flights': user_flights, 'form': form})
