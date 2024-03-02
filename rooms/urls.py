from django.urls import path
from .views import *


"""
API endpoints for rooms
api/rooms/list/ - GET request
    Optional fields: hotel_id
    Returns: list of rooms
api/rooms/create/ - POST request
    Required fields: hotel_id, room_type, price_per_night, room_number
    Returns: created room
api/rooms/update/<room_id>/ - PUT request
    Required fields: None
    Optional fields: hotel_id, room_type, price_per_night, room_number
    Returns: updated room
api/rooms/delete/<room_id>/ - DELETE request
    Required fields: None
    Returns: None
"""
urlpatterns = [
    path("list/", ListView, name="list"),
    path("create/", CreateView, name="create"),
    path("update/<room_id>/", UpdateView, name="update"),
    path("delete/<room_id>/", DeleteView, name="delete"),
]
