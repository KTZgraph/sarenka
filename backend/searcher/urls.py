
from django.urls import path
from searcher.views import CVESearchView, CensysHostSearchView, ListVendors

urlpatterns = [
    path('cve/<str:code>', CVESearchView.as_view(), name="get_by_cve"),
    path('list_vendors/', ListVendors.as_view()),
    path('censys/<str:ip_address>', CensysHostSearchView.as_view(), name="get_censys_host_data"),
]
