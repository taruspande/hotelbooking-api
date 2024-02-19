from django.db import models
import uuid

class Hotel(models.Model):
    hotel_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    free_wifi = models.BooleanField(default=False)
    pool = models.BooleanField(default=False)
    spa = models.BooleanField(default=False)
    restaurant = models.BooleanField(default=False)
    laundry = models.BooleanField(default=False)
    checkin_time = models.TimeField()
    checkout_time = models.TimeField()
    
    def __str__(self):
        return self.name
    
    