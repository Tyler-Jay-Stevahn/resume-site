from django.db import models
from django.utils import timezone

# Create your models here.
class registration_data(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    pub_date = models.DateField(default=timezone.now())

class medical_data(modesl.Model):
    L_CORE = models.IntegerField(max_length=4)
    L_SURF = models.IntegerField(max_length=4)
    L_O2 = models.IntegerField(max_length=4)
    L_BP = models.IntegerField(max_length=4)
    SURF_STBL = models.IntegerField(max_length=4)
    CORE_STBL = models.IntegerField(max_length=4)
    BP_STBL = models.IntegerField(max_length=4)
    COMFORT = models.IntegerField(max_length=4)
    DESCISION = models.IntegerField(max_length=4)
