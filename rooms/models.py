from django.db import models
from hotels.models import Hotel
import uuid


class Room(models.Model):
    class room_types(models.IntegerChoices):
        HU = 1
        STU = 2
        BR1 = 3
        BR2 = 4

    room_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.IntegerField(choices=room_types.choices, default=room_types.HU)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    room_number = models.IntegerField()

    def get_room_type(self):
        return self.room_types(self.room_type)

    def __str__(self):
        return str(self.room_id)
