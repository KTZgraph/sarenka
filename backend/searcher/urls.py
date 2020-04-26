
from django.urls import path
from searcher.views import get_by_cve

urlpatterns = [
    path('cve/', get_by_cve, name="get_by_cve"),
]