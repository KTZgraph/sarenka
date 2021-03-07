from django.urls import path

from .views import CredentialsAPI

urlpatterns = [
    path('credentials/', CredentialsAPI.as_view(), name='credentials'),
]
