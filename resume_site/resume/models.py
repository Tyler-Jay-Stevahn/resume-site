from django.db import models
from django.utils import timezone

# Create your models here.
class registration_data(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    entry_date = models.DateField(default=timezone.now())

class medical_data(models.Model):
    L_CORE = models.IntegerField()
    L_SURF = models.IntegerField()
    L_O2 = models.IntegerField()
    L_BP = models.IntegerField()
    SURF_STBL = models.IntegerField()
    CORE_STBL = models.IntegerField()
    BP_STBL = models.IntegerField()
    COMFORT = models.IntegerField()
    DESCISION = models.IntegerField()
