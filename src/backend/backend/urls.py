from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework import schemas
from rest_framework.documentation import include_docs_urls



urlpatterns = [
    path("admin/", admin.site.urls),
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
]
