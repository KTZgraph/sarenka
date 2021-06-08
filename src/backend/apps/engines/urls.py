from django.urls import path

from .views import CensysCredentials, CredentialsShodan

app_name = 'engines'

urlpatterns = [
    # path('credentials_censys/', CensysCredentials.as_view(), name='credentials_censys'),
    # path('credentials_shodan/', CredentialsShodan.as_view(), name='credentials_shodan'),
]
