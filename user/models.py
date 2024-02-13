from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


# Create your models here.


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, password=None, **extra_fields):
        if username is None:
            raise ValueError("Users must have a username")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True, blank=False, null=False)
    name = models.CharField(max_length=255)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.name


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "name", "password"]

    def validate(self, attrs):
        username = attrs.get("username", "")
        if not username.isalnum():
            raise serializers.ValidationError(
                "The username should only contain alphanumeric characters"
            )
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"], name=validated_data["name"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
