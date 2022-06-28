from django.db import models

# Create your models here.


class Phone(models.Model):
    firstname = models.CharField(max_length=20, unique=True)
    lastname = models.CharField(max_length=20, default='Peter')
    number = models.CharField(max_length=20, unique=True)
