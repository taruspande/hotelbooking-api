from django.db import models
from django.contrib.auth.models import User
from hotels.models import Hotel
from django.core.exceptions import ValidationError
import uuid


class Review(models.Model):
    review_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    title = models.CharField(max_length=255)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.review_id)

    def clean(self):
        if not 1 <= self.rating <= 5:
            raise ValidationError({"rating": "Invalid rating"})

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Review, self).save(*args, **kwargs)
