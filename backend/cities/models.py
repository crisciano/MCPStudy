from django.db import models
from core.models import BaseModel


class City(BaseModel):
    name = models.CharField(max_length=100)
    state = models.ForeignKey('states.State', on_delete=models.PROTECT, related_name='cities')

    def __str__(self):
        return f"{self.name}, {self.state.abbreviation}"