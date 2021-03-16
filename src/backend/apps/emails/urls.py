from django.urls import path

from .views import Protonmail

urlpatterns = [
    path('protonmail/', Protonmail.as_view(), name='protonmail'),
]
