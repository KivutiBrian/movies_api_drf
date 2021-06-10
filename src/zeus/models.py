from django.db import models
from django.utils.translation import activate

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=250, null=False)
    active = models.BooleanField(default=True)
    