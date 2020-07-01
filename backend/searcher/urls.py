
from django.urls import path
from searcher.views import CVESearchView, CensysHostSearchView

urlpatterns = [
    path('cve/<str:code>', CVESearchView.as_view(), name="get_by_cve"),
    path('censys/<str:ip_address>', CensysHostSearchView.as_view(), name="get_censys_host_data"),
]