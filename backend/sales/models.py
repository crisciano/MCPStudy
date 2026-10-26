from django.db import models
from core.models import BaseModel


class Sale(BaseModel):
    vehicle = models.ForeignKey('vehicles.Vehicle', on_delete=models.PROTECT, related_name='sales')
    salespeople = models.ForeignKey('salespeople.salespeople', on_delete=models.PROTECT, related_name='sales')
    customer = models.ForeignKey('customers.Customer', on_delete=models.PROTECT, related_name='sales')
    dealership = models.ForeignKey('dealerships.Dealership', on_delete=models.PROTECT, related_name='sales')
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Sale of {self.vehicle.name} to {self.customer.name}"