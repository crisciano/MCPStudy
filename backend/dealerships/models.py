from django.db import models
from core.models import BaseModel


class Dealership(BaseModel):
    name = models.CharField(max_length=150)
    city = models.ForeignKey('cities.City', on_delete=models.PROTECT, related_name='dealerships')

    def __str__(self):
        return self.name