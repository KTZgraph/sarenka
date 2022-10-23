# https://youtu.be/rxRYEXBmM88?t=2102

from dataclasses import field
from rest_framework import serializers
from django.contrib.auth import get_user_model


# wywołanie modelu user
User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password")

    def create(self, validated_data):
        """Nadpisanie istneijącej metody"""
        # tworzenie obiektu Usera ze zwaliddowanych danych
        user = User.objects.create_user(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            # serializer wie jak zwalidowac email , bo w modelach ma typ emailField
            # trzeba by vcoś takiego pisać, jakbyś nie mieli modelu
            # serializers.EmailField()
            email=validated_data["email"],
            password=validated_data["password"],
        )

        return user
