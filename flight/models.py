from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Airline(models.Model):
    name = models.CharField(max_length=100)
    found_year = models.PositiveIntegerField()
    flies_outside_europe = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Hot_Air_Baloon(models.Model):
    type = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    max_passengers = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.type} by {self.manufacturer}"

class Pilot(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_year = models.PositiveIntegerField()
    total_hours_flown = models.PositiveIntegerField()
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, null=True, blank=True)  # Додаваме врска со Airline

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Flight(models.Model):
    flight_number = models.CharField(max_length=100)
    departure_airport = models.CharField(max_length=100)
    arrival_airport = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    balloon = models.ForeignKey(Hot_Air_Baloon, on_delete=models.CASCADE, blank=True, null=True),
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.flight_number} from {self.departure_airport} to {self.arrival_airport}"