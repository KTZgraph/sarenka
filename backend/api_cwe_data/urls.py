from django.urls import path
from api_cwe_data.views import CWETop25

urlpatterns = [
    path("", CWETop25.as_view(), name="cwe_data")
]