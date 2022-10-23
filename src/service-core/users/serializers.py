# https://youtu.be/rxRYEXBmM88?t=2102

from dataclasses import field
from rest_framework import serializers
from django.contrib.auth import get_user_model


# wywołanie modelu user
User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
