from django.contrib.auth.models import User
from rest_framework import serializers


# Create your serializers here.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "password"]

    def create(self, validated_data):
        data = {"username": validated_data["username"]}
        if validated_data.__contains__("first_name"):
            data["first_name"] = validated_data["first_name"]
        if validated_data.__contains__("last_name"):
            data["last_name"] = validated_data["last_name"]
        user = User.objects.create(**data)
        user.set_password(validated_data["password"])
        user.save()
        return user
