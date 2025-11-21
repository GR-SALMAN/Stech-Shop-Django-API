from django.db import models

# Create your models here.
from django.db import models


class Product(models.Model):  # No id field here
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    info = models.JSONField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField()
    type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.brand} {self.model}"
