from django.db import models
from rooms.models import Room
from django.contrib.auth.models import User
import uuid

# Create your models here.


class Booking(models.Model):
    booking_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
