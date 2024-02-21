from django.db import models

class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
