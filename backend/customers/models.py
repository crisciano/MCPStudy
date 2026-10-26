from django.db import models
from core.models import BaseModel


class Customer(BaseModel):
    name = models.CharField(max_length=150)
    address = models.TextField()

    def __str__(self):
        return self.name