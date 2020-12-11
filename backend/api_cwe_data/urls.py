from django.urls import path
from api_cwe_data.views import CWETop25, CWEData

urlpatterns = [
    path("", CWETop25.as_view(), name="cwe_top_25"),
    # path("top_25", CWETop25.as_view(), name="cwe_top_25"),
    path("<str:id_cwe>", CWEData.as_view(), name="cwe_data")

]