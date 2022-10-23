from rest_framework.views import APIView
from rest_framework.response import Response

# https://www.django-rest-framework.org/api-guide/status-codes/
from rest_framework import permissions, status

# też wywołanie modelu User z Django
from django.contrib.auth import get_user_model

User = get_user_model()

# import mojego serializera
from .serializers import UserCreateSerializer


class RegisterView(APIView):
    def post(self, request):
        """http://localhost:8000/api/users/register
        {
            "first_name": "John",
            "last_name": "Doe",
            "email": "johndoe@gmail.com",
            "password": "password"
        }

        zwrotka
        {
            "id": 2,
            "password": "pbkdf2_sha256$390000$Koyy4P5zDR65Flfb3gOtSp$IjKH1SjwLbhRclJ7TjRd/ukS/RrXRl4WYrp5+VB7DCQ=",
            "last_login": null,
            "is_superuser": false,
            "first_name": "John",
            "last_name": "Doe",
            "email": "johndoe@gmail.com",
            "is_active": true,
            "is_staff": false,
            "groups": [],
            "user_permissions": []
        }
        """

        data = request.data

        # nadpisujemy Managera z modelu User z Django
        # pola jak do service-core\users\models.py klasy UserAccountManager
        # metoda .create_user zwraca Usera jest         return user
        #  w linii 27
        # usuwam tę linię, bo serializatorem będe tworzyć obiekt
        # user = User.objects.create_user(first_name, last_name, email, password)

        serializer = UserCreateSerializer(data=data)
        # dprawdzam, czy te pola są valid
        if not serializer.is_valid():
            # jak dane nieprawidłowe to zwrotka 400
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # jak dane prawidłowe to tworze usera
        # metoda create na tym obiekcie serializator to nasza przeciążona  metoda
        # .validated_data to atrybut obiektu serializatora
        user = serializer.create(serializer.validated_data)
        # teraz dopiero user ma atrybuty .data potrzebny do zwrotki
        user = UserCreateSerializer(user)

        # zwraca usera dane jako zwrotkę
        return Response(user.data, status=status.HTTP_201_CREATED)


class RetrieveUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        pass
