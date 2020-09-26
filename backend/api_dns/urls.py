from django.urls import path
from api_dns.views import ARecordAPIView

urlpatterns = [
    path("<str:fqdn>/", ARecordAPIView.as_view(), name="dns_record")
]