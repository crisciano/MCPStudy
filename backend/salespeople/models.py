from django.db import models
from core.models import BaseModel


class Salespeople(BaseModel):
    name = models.CharField(max_length=150)
    dealership = models.ForeignKey('dealerships.Dealership', on_delete=models.CASCADE, related_name='salespeople')

    def __str__(self):
        return self.name