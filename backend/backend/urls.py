"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="SARENKA API",
        default_version='v1',
        description="Information gathering tool.",
        terms_of_service="test terms",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="Test License"),
        x_logo={
            "url": "https://github.com/pawlaczyk/sarenka/blob/master/logo.png",
            "backgroundColor": "#FFFFFF"
        }
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', include("api_searcher.urls")),
    path('api_cheat_sheet/', include("api_cheat_sheet.urls")),
    path('analyzer/', include("api_analyzer.urls")),
    path('dns/', include("api_dns.urls")),
    path('reports/', include("reports.urls")),

    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
