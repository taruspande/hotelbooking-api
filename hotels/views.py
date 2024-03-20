from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rooms.models import Room
from reviews.models import Review


def gen_keywords(name):
    min_word_length = 3
    avoid = [
        "the",
        "to",
        "i",
        "am",
        "is",
        "are",
        "he",
        "she",
        "a",
        "an",
        "and",
        "here",
        "there",
        "can",
        "could",
        "were",
        "has",
        "have",
        "had",
        "been",
        "of",
        "into",
        "this",
        "there",
    ]
    name = name.lower()
    words = name.split()
    keywords = []
    for word in words:
        if len(word) >= min_word_length and word not in avoid:
            keywords.append(word)
    return keywords


@api_view(["GET"])
def hotel_list(request):
    try:
        filters = {}
        if "city" in request.query_params:
            filters["city"] = request.query_params["city"]
        if "stars" in request.query_params:
            stars = eval(request.query_params["stars"])
        else:
            stars = [1, 2, 3, 4, 5]
        if "free_wifi" in request.query_params:
            filters["free_wifi"] = eval(request.query_params["free_wifi"])
        if "pool" in request.query_params:
            filters["pool"] = eval(request.query_params["pool"])
        if "spa" in request.query_params:
            filters["spa"] = eval(request.query_params["spa"])
        if "gym" in request.query_params:
            filters["gym"] = eval(request.query_params["gym"])
        if "restaurant" in request.query_params:
            filters["restaurant"] = eval(request.query_params["restaurant"])
        if "laundry" in request.query_params:
            filters["laundry"] = eval(request.query_params["laundry"])
        hotels = Hotel.objects.filter(**filters, stars__in=stars)
        if "name" in request.query_params:
            name = request.query_params["name"]
            keywords = gen_keywords(name)
            hotel_list = []
            for hotel in hotels:
                hotel_keywords = gen_keywords(hotel.name)
                if all(keyword in hotel_keywords for keyword in keywords):
                    hotel_list.append(hotel)
        serializer = HotelSerializer(hotel_list, many=True)
        for hotel in serializer.data:
            id = hotel["hotel_id"]
            rooms = Room.objects.filter(hotel_id=id)
            room_types = []
            min_price = 0 if len(rooms) == 0 else rooms[0].price_per_night
            max_price = min_price
            average_price = 0
            for room in rooms:
                if room.room_type not in room_types:
                    room_types.append(room.room_type)
                if room.price_per_night < min_price:
                    min_price = room.price_per_night
                if room.price_per_night > max_price:
                    max_price = room.price_per_night
                average_price += room.price_per_night
            hotel["room_types"] = room_types
            hotel["min_price"] = min_price
            hotel["max_price"] = max_price
            hotel["average_price"] = (
                0 if len(rooms) == 0 else (average_price / len(rooms))
            )
            reviews = Review.objects.filter(hotel_id=id)
            hotel["reviews"] = len(reviews)
            rating = 0
            for review in reviews:
                rating += review.rating
            hotel["rating"] = 0 if len(reviews) == 0 else (rating / len(reviews))
        return Response(serializer.data)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def create_hotel(request):
    try:
        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def update_hotel(request, hotel_id):
    try:
        name = request.data.get("name")
        address = request.data.get("address")
        city = request.data.get("city")
        latitude = request.data.get("latitude")
        longitude = request.data.get("longitude")
        contact = request.data.get("contact")
        free_wifi = request.data.get("free_wifi")
        pool = request.data.get("pool")
        spa = request.data.get("spa")
        gym = request.data.get("gym")
        restaurant = request.data.get("restaurant")
        laundry = request.data.get("laundry")
        stars = request.data.get("stars")
        overview = request.data.get("overview")
        nearby = request.data.get("nearby")
        checkin_time = request.data.get("checkin_time")
        checkout_time = request.data.get("checkout_time")
        hotel = Hotel.objects.get(hotel_id=hotel_id)
        data = {
            "hotel_id": hotel_id,
            "name": name if name else hotel.name,
            "address": address if address else hotel.address,
            "city": city if city else hotel.city,
            "latitude": latitude if latitude else hotel.latitude,
            "longitude": longitude if longitude else hotel.longitude,
            "contact": contact if contact else hotel.contact,
            "free_wifi": free_wifi if free_wifi else hotel.free_wifi,
            "pool": pool if pool else hotel.pool,
            "spa": spa if spa else hotel.spa,
            "gym": gym if gym else hotel.gym,
            "restaurant": restaurant if restaurant else hotel.restaurant,
            "laundry": laundry if laundry else hotel.laundry,
            "stars": stars if stars else hotel.stars,
            "overview": overview if overview else hotel.overview,
            "nearby": nearby if nearby else hotel.nearby,
            "checkin_time": checkin_time if checkin_time else hotel.checkin_time,
            "checkout_time": checkout_time if checkout_time else hotel.checkout_time,
        }
        serializer = HotelSerializer(hotel, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Hotel.DoesNotExist:
        return Response({"error": "Hotel not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_hotel(request, hotel_id):
    try:
        hotel = Hotel.objects.get(hotel_id=hotel_id)
        hotel.delete()
        return Response(
            {"message": "Hotel deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )
    except Hotel.DoesNotExist:
        return Response({"error": "Hotel not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
