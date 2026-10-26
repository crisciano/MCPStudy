from django.contrib import admin
from .models import Salespeople


@admin.register(Salespeople)
class SalespeopleAdmin(admin.ModelAdmin):
    list_display = ('name', 'dealership', 'created_at')
    search_fields = ('name', 'dealership__name')
    list_filter = ('dealership',)
    autocomplete_fields = ()
    ordering = ('name',)