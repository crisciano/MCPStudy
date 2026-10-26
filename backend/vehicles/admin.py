from django.contrib import admin
from .models import Vehicle


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('name', 'vehicle_type', 'price', 'created_at')
    search_fields = ('name', 'vehicle_type')
    list_filter = ('vehicle_type',)
    ordering = ('name',)