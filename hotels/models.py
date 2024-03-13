from django.db import models
from django.core.exceptions import ValidationError
import uuid


class Hotel(models.Model):
    hotel_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=28.614367)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=77.199530)
    contact = models.IntegerField()
    free_wifi = models.BooleanField(default=False)
    pool = models.BooleanField(default=False)
    spa = models.BooleanField(default=False)
    gym = models.BooleanField(default=False)
    restaurant = models.BooleanField(default=False)
    laundry = models.BooleanField(default=False)
    stars = models.IntegerField(default=1)
    overview = models.TextField(default="")
    nearby = models.TextField(default="")
    checkin_time = models.TimeField()
    checkout_time = models.TimeField()

    def __str__(self):
        return str(self.hotel_id)

    def clean(self):
        if not len(str(self.contact)) == 10:
            raise ValidationError({"contact": "Invalid contact number"})
        if not 1 <= self.stars <= 5:
            raise ValidationError({"stars": "Invalid number of stars"})
        if self.checkin_time <= self.checkout_time:
            raise ValidationError({"checkout_time": "Invalid checkout time"})
        if abs(self.latitude) > 90:
            raise ValidationError({"latitude": "Invalid latitude"})
        if abs(self.longitude) > 180:
            raise ValidationError({"longitude": "Invalid longitude"})

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Hotel, self).save(*args, **kwargs)
