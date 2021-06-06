from django.urls import path

from .views import CredentialsAPI

app_name = 'engines'

urlpatterns = [
    path('credentials/', CredentialsAPI.as_view(), name='credentials'),
]
