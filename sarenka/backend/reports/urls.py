from django.urls import path
from reports.views import GeneratePdfHostInfo, GeneratePdfHardware


urlpatterns = [

    path('host_info/<str:ip_address>', GeneratePdfHostInfo.as_view(), name="get_censys_host_data"),
    path('hardware_info/', GeneratePdfHardware.as_view(), name="hardware_report"),

]