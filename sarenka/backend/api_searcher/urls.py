from django.urls import path
from .views.search_engines import (CensysHostSearchView,
                                   ShodanHostSearchView,
                                   login_required_view,
                                   SearcherView)

from .views.vendor_list import VendorListView
from .views.dns import DNSSearcherView
from .views.user_credentials import UserCredentialsView
from .views.windows import NetworkLocalView, LocalView, HardwareView, RegistryView

urlpatterns = [
    # dodanie kluczy użytkownika do serwisów trzeich
    path('user_credentials', UserCredentialsView.as_view(), name="user_credentials"),

    path('list_vendors', VendorListView.as_view()),

    path('censys/<str:ip_address>', CensysHostSearchView.as_view(), name="get_censys_host_data"),
    path('shodan/<str:ip_address>', ShodanHostSearchView.as_view(), name="get_shodan_host_data"),
    path('search/<str:host>', SearcherView.as_view(), name="search"),

    path('login_required_view/<str:cve_code>', login_required_view, name="login_required_view"),

    path("dns/<str:host>", DNSSearcherView.as_view(), name="dns_record"),

    path('local', LocalView.as_view(), name="local_windows"),
    path('local/registry', RegistryView.as_view(), name="registry_windows"),
    path('local/hardware', HardwareView.as_view(), name="hardware_windows"),
    path('local/network', NetworkLocalView.as_view(), name="network_windows"),
]
