from django.db import models

# Create your models here.
class Avto(models.Model):
    model = models.CharField(max_length=100, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    year = models.CharField(max_length=100, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)

    def __str__(self) -> str:
        return self.model