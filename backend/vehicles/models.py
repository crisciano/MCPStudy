from django.db import models
from core.models import BaseModel


class Vehicle(BaseModel):
    name = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name