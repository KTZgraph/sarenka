from django.urls import path
from api_dns.views import ARecordView

urlpatterns = [
    path("<str:fqdn>", ARecordView.as_view(), name="dns_record")
]