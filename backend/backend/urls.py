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
    path('cheat_sheet/', include("api_cheat_sheet.urls")),
    path('analyzer/', include("api_analyzer.urls")),
    path('dns/', include("api_dns.urls")),
    path('reports/', include("reports.urls")),
    path('graphql/', GraphQLView.as_view(graphiql=True)),

    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
