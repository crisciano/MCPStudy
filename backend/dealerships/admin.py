from django.contrib import admin

from .models import Dealership

@admin.register(Dealership)
class DealershipAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state', 'created_at')
    search_fields = ('name', 'city__name', 'state__name')
    list_filter = ('city__state',)
    autocomplete_fields = ('city',)
    ordering = ('name',)
    
    def state(self, obj):
        return obj.city.state.name

