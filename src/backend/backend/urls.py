from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="SARENKA",
      default_version='0.0.1',
      description="OSINT",
      terms_of_service="",
      contact=openapi.Contact(email="pawlaczyk"),
      license=openapi.License(name="MIT"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/core/', include('apps.core.urls')),
    path('api/emails/', include('apps.emails.urls')),
    path('api/cheat_sheets/', include('apps.cheat_sheets.urls')),
    path('api/engines/', include('apps.engines.urls')),
    path('api/products/', include('apps.products.urls')),
    path('api/search/', include('apps.search.urls')),
    path('api/technologies/', include('apps.technologies.urls')),
    path('api/tools/', include('apps.tools.urls')),
    path('api/universities/', include('apps.universities.urls')),
    path('api/vendors/', include('apps.vendors.urls')),
    path('api/vulns/', include('apps.vulnerabilities.urls')),
    path('api/ataner/', include('apps.ataner.urls')),
]
