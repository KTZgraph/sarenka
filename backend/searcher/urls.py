
from django.urls import path
from searcher.views import CVESearchView
from searcher.views import ListVendors




urlpatterns = [
    path('cve/<str:code>', CVESearchView.as_view(), name="get_by_cve"),
    path('list_vendors/', ListVendors.as_view()),

]