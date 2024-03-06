from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.hotel_list, name='hotel-list'),
    path('create/', views.create_hotel, name='create-hotel'),
    path('update/<uuid:hotel_id>/', views.update_hotel, name='update-hotel'),
    path('delete/<uuid:hotel_id>/', views.delete_hotel, name='delete-hotel'),
]
