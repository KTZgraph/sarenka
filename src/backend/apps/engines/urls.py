from rest_framework.routers import DefaultRouter

from .views import CensysCredentialsView, ShodanCredentialsView

app_name = 'engines'

router = DefaultRouter()
router.register('censys-credentials', CensysCredentialsView, basename='censys-credentials')
router.register('shodan-credentials', ShodanCredentialsView, basename='shodan-credentials')
urlpatterns = router.urls
