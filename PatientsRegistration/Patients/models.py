from logging import PercentStyle
from django.db import models

# Create your models here.

class Patient(models.Model):
    name            = models.CharField(max_length=30)
    last_name       = models.CharField(max_length=30)
    date_of_birth   = models.DateField()
    pesel           = models.DecimalField(decimal_places = 0, max_digits=11)