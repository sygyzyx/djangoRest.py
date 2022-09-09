from email.headerregistry import Address
from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.
class Data(models.Model):
    Name = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)