from django.contrib import admin
from .models import State


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation', 'created_at')
    search_fields = ('name', 'abbreviation')
    ordering = ('name',)