from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CensysCredentialsView, ShodanCredentialsView, get_shodan_queries

app_name = 'engines'

router = DefaultRouter()
router.register('censys-credentials', CensysCredentialsView, basename='censys-credentials')
router.register('shodan-credentials', ShodanCredentialsView, basename='shodan-credentials')

urlpatterns = [
  path('shodan-queries/', get_shodan_queries, name="shodan-queries"),
]

urlpatterns += router.urls
