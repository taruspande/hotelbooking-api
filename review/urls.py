from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.review_create, name='review-create'),
    path('delete/<uuid:review_id>/', views.review_delete, name='review-delete'),
    path('update/<uuid:review_id>/', views.review_update, name='review-update'),
    path('hotel/<uuid:hotel_id>/', views.hotel_reviews, name='hotel-reviews'),
    path('user/<int:user_id>/', views.user_reviews, name='user-reviews'),
]
