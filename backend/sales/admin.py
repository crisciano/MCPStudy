from django.contrib import admin
from .models import Sale


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'vehicle',
        'customer',
        'salespeople',
        'dealership',
        'sale_price',
        'created_at'
    )
    list_filter = ('dealership', 'salespeople', 'created_at')
    search_fields = ('vehicle__name', 'customer__name', 'salespeople__name')
    autocomplete_fields = ('vehicle', 'salespeople', 'customer')
    ordering = ('-created_at',)