from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


# Create your views here.
@api_view(["POST"])
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


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def review_delete(request, review_id):
    try:
        review = Review.objects.get(review_id=review_id)
        if review.user_id != request.user.id:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except (ValueError, TypeError, Review.DoesNotExist):
        return Response("Review not found", status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def review_update(request, review_id):
    try:
        review = Review.objects.get(review_id=review_id)
        if review.user_id != request.user.id:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        hotel_id = request.data.get("hotel_id")
        rating = request.data.get("rating")
        title = request.data.get("title")
        comment = request.data.get("comment")
        data = {
            "review_id": review_id,
            "hotel_id": hotel_id if hotel_id else str(review.hotel_id),
            "user_id": review.user_id,
            "rating": rating if rating else review.rating,
            "title": title if title else review.title,
            "comment": comment if comment else review.comment,
        }
        serializer = ReviewSerializer(review, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except (ValueError, TypeError, Review.DoesNotExist):
        return Response("Review not found", status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def hotel_reviews(request):
    try:
        hotel_id = request.query_params.get("hotel_id")
        reviews = Review.objects.filter(hotel_id=hotel_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_reviews(request):
    try:
        user_id = request.user.id
        reviews = Review.objects.filter(user_id=user_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
