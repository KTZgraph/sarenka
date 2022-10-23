# https://youtu.be/rxRYEXBmM88?t=2102

# wyjątek ValidationError Django z sarenka\src\service-core\env\Lib\site-packages\django\core\exceptions.py
from django.core import exceptions
from rest_framework import serializers
from django.contrib.auth import get_user_model

# dostęp do walidacja hasła widocnze w settings.py AUTH_PASSWORD_VALIDATORS
from django.contrib.auth.password_validation import validate_password


# wywołanie modelu user
User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password")

    def validate(self, data):
        """nadpisanie metody - zeby zwykły user tworozny przez REST API tez miał silne hasło jak admin"""
        # extra validatiorns

        # trzeba wyciągnac dane z pola password
        password = data.get("password")
        # opcjonalnie można podać usera do metoda walidacji hasła z Django
        # **data wypakowanie danych
        user = User(**data)

        try:
            # dostęp do walidacja hasła widocnze w settings.py AUTH_PASSWORD_VALIDATORS
            # zweraca None jak wszytko ok, w przeciwnym wuypadku zwróci ValidationError
            # z sarenka\src\service-core\env\Lib\site-packages\django\contrib\auth\password_validation.py
            # validate_password(password)
            # przekazuję ocpjonalny mparametre user
            validate_password(password, user)
        except exceptions.ValidationError as e:
            # wyjątek ValidationError Django z sarenka\src\service-core\env\Lib\site-packages\django\core\exceptions.py
            # teraz ten wyjatek z Django jako obiekt e - chcę zroiić jako error serializera
            # WARNING - mega ciekawy sposób na zwrotkę błedu Django jako błedu serialzatora
            # https://youtu.be/rxRYEXBmM88?t=3272
            # gloablnie dostępna funkcja z rest_framework ktora jeako arguiment bierze exceptions
            # as_serializer_error(exc) sarenka\src\service-core\env\Lib\site-packages\rest_framework\serializers.py
            #  'NON_FIELD_ERRORS_KEY': 'non_field_errors', sarenka\src\service-core\env\Lib\site-packages\rest_framework\settings.py
            serializers_errors = serializers.as_serializer_error(e)
            # zamiast zwrotki ttuaj rzucam sój wyjatek
            raise exceptions.ValidationError(
                # rzucam wyjatek typu Django z wiadomoscią który jest dostępny w obiektcie błedu serialziatora w polu 'non_field_errors'
                # bo chcę mieć zwrot jakby walidator był wbusdowany w django
                {"password": serializers_errors["non_field_errors"]}
            )

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


class UserSerializer(serializers.ModelSerializer):
    """Seriaslizer gdize nie zwraacam hasła do zwrotki API REST"""

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")
