from django.contrib import admin
from .models import City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'state', 'created_at')
    search_fields = ('name', 'state__name')
    list_filter = ('state',)
    autocomplete_fields = ('state',)
    ordering = ('name',)
    