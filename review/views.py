from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .models import Review
from .serializers import ReviewSerializer
from django.shortcuts import get_object_or_404
from uuid import UUID 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def review_create(request):
    try:
        user_id = request.user.id
        data = request.data
        data["user_id"] = user_id
      
        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def review_delete(request, review_id):
    try:
        review_uuid = UUID(review_id)
        review = get_object_or_404(Review, review_id=review_uuid)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except (ValueError, TypeError, Review.DoesNotExist):
        return Response("Review not found", status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def review_update(request, review_id):
    try:
        review_uuid = UUID(review_id)
        review = get_object_or_404(Review, review_id=review_uuid)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except (ValueError, TypeError, Review.DoesNotExist):
        return Response("Review not found", status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def hotel_reviews(request, hotel_id):
    try:
        reviews = Review.objects.filter(hotel_id=hotel_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def user_reviews(request, user_id):
    try:
        reviews = Review.objects.filter(user_id=user_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)