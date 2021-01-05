from django.urls import path
from .views import CVESearchView, CWETop25, CWEData, CWEAllView, CVEDetailsAllView, CWEDetailsAllView, \
    AddCWEandCVE

urlpatterns = [
    path('cve/<str:cve_id>', CVESearchView.as_view(), name="get_by_cve"),
    path('cve/all/<str:page>', CVEDetailsAllView.as_view(), name="cve_all"),

    path('cwe', CWETop25.as_view(), name="cwe_top_25"),
    path('cwe/all', CWEAllView.as_view(), name="cwe_all"),
    path('cwe/all/<str:page>', CWEDetailsAllView.as_view(), name="cwe_all_details"),
    path('cwe/<str:id_cwe>', CWEData.as_view(), name="get_by_cwe"),
    path('cwe/add', AddCWEandCVE.as_view(), name="cwe_add"),

]
