
from django.urls import path
from .views import (DNSSearcherView,
                    CVESearchView,
                    CensysHostSearchView,
                    ListVendors,
                    login_required_view,
                    CWETop25,
                    CWEData,
                    CommandsWindows,
                    LocalWindows,
                    NetworkLocal,
                    SearcherView)

urlpatterns = [
    path('cve/<str:code>', CVESearchView.as_view(), name="get_by_cve"),
    path('cwe', CWETop25.as_view(), name="cwe_top_25"),
    # path("top_25", CWETop25.as_view(), name="cwe_top_25"),
    path('cwe/<str:id_cwe>', CWEData.as_view(), name="get_by_cwe"),
    path('list_vendors', ListVendors.as_view()),
    path('censys/<str:ip_address>', CensysHostSearchView.as_view(), name="get_censys_host_data"),
    path('search/<str:host>', SearcherView.as_view(), name="search"),
    path('login_required_view/<str:cve_code>', login_required_view, name="login_required_view"),
    path("dns/<str:host>", DNSSearcherView.as_view(), name="dns_record"),
    path('local/registry', LocalWindows.as_view(), name="windows"),
    path('local/hardware', CommandsWindows.as_view(), name="hardware_windows"),
    path('local/network', NetworkLocal.as_view(), name="network_windows"),
]
