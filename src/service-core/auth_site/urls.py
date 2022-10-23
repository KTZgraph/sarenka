from django.contrib import admin
from django.urls import path, include

# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    # https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    # ściezka do pliku urls z apilakci "users"
    path("api/users/", include("users.urls")),
    path("admin/", admin.site.urls),
]
