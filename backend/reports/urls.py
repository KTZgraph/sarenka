from django.urls import path
from reports.views import GeneratePdf


urlpatterns = [
    path('<str:ip_address>', GeneratePdf.as_view(), name="get_censys_host_data"),
    
]