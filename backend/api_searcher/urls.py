
from django.urls import path
from .views import ARecordView, CVESearchView, CensysHostSearchView, ListVendors, login_required_view, CWETop25, CWEData

urlpatterns = [
    path('cve/<str:code>', CVESearchView.as_view(), name="get_by_cve"),
    path('cwe', CWETop25.as_view(), name="cwe_top_25"),
    # path("top_25", CWETop25.as_view(), name="cwe_top_25"),
    path('cwe/<str:id_cwe>', CWEData.as_view(), name="get_by_cwe"),
    path('list_vendors', ListVendors.as_view()),
    path('censys/<str:ip_address>', CensysHostSearchView.as_view(), name="get_censys_host_data"),
    path('login_required_view/<str:cve_code>', login_required_view, name="login_required_view"),
    path("dns/<str:fqdn>", ARecordView.as_view(), name="dns_record"),
]
