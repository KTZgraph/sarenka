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
        first_name = data["first_name"]
        last_name = data["last_name"]
        email = data["email"]
        password = data["password"]

        # nadpisujemy Managera z modelu User z Django
        # pola jak do service-core\users\models.py klasy UserAccountManager
        # metoda .create_user zwraca Usera jest         return user
        #  w linii 27
        # usuwam tę linię, bo serializatorem będe tworzyć obiekt
        # user = User.objects.create_user(first_name, last_name, email, password)

        serializer = UserCreateSerializer(
            data={
                # sposób na przekazanie danych do serializatora
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "password": password,
            }
        )

        # zwraca usera dane jako zwrotkę
        return Response(user.data, status=status.HTTP_201_CREATED)


class RetrieveUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        pass
