from django.contrib import admin
from .models import Airline, Hot_Air_Baloon, Pilot, Flight


class PilotInline(admin.TabularInline):
    model = Pilot
    extra = 1
    list_display = ('first_name', 'last_name', 'birth_year', 'total_hours_flown')


@admin.register(Airline)
class AirlineAdmin(admin.ModelAdmin):
    inlines = [PilotInline]
    list_display = ('name', 'found_year', 'flies_outside_europe')

@admin.register(Hot_Air_Baloon)
class HotAirBaloonAdmin(admin.ModelAdmin):
    list_display = ('type', 'manufacturer', 'max_passengers')

@admin.register(Pilot)
class PilotAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_number', 'departure_airport', 'arrival_airport', 'created_by', 'airline', 'balloon', 'pilot')

    def has_change_permission(self, request, obj=None):
        if obj is not None:
            return obj.created_by == request.user or request.user.is_superuser
        return True

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        return False