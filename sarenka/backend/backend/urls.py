from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from graphene_django.views import GraphQLView

schema_view = get_schema_view(
    openapi.Info(
        title="SARENKA API",
        default_version='v1',
        description="Open Source Intelligence (OSINT) tool .",
        terms_of_service="test terms",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="MIT"),
        x_logo={ # to nie dizała na zmiane kolorkow i logo :<
            "url": "https://github.com/pawlaczyk/sarenka/blob/master/logo.png",
            "backgroundColor": "#CC0"
        }
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("api_searcher.urls")),
    path('vulns/', include("api_vulnerabilities.urls")),
    path('tools/', include("api_tools.urls")),
    path('reports/', include("reports.urls")),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
