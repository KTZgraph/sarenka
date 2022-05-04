from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import schemas
from rest_framework.documentation import include_docs_urls

schema_view = get_schema_view(
    openapi.Info(
        title="SARENKA",
        default_version="0.0.1",
        description="SARENKA API",
        terms_of_service="",
        contact=openapi.Contact(email="pawlaczyk"),
        license=openapi.License(name="MIT"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("api/emails/", include("apps.emails.urls")),
    path("api/cheat_sheets/", include("apps.cheat_sheets.urls")),
    path("api/core/", include("apps.core.urls")),
    path("api/engines/", include("apps.engines.urls")),
    path("api/notes/", include("apps.notes.urls")),
    path("api/products/", include("apps.products.urls")),
    path("api/search/", include("apps.search.urls")),
    path("api/technologies/", include("apps.technologies.urls")),
    path("api/tools/", include("apps.tools.urls")),
    path("api/universities/", include("apps.universities.urls")),
    path("api/users/", include("apps.users.urls")),
    path("api/vendors/", include("apps.vendors.urls")),
    path("api/vulns/", include("apps.vulnerabilities.api.urls")),
    # https://www.django-rest-framework.org/api-guide/schemas/
    path("docs/", include_docs_urls(title="SarenkaAPI")),
    path(
        "schema",
        schemas.get_schema_view(
            title="SarenkaAPI",
            description="API for for the SARENKA",
            version="0.0.1",
        ),
        name="openapi-schema",
    ),
]
