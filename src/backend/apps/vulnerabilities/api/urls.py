"""
http://127.0.0.1:8000/api/vulns/vector/1/

#with slash at the end doesn't work
http://127.0.0.1:8000/api/vulns/vector-list/search/?severity=2
http://127.0.0.1:8000/api/vulns/vector-list/search/?severity=medium
http://127.0.0.1:8000/api/vulns/vector-list/search/?cve=cve-1
http://127.0.0.1:8000/api/vulns/vector-list/search/?severity=2&cve=cve-1
http://127.0.0.1:8000/api/vulns/vector-list/search/?code=QVY6TC9BQzo=
http://127.0.0.1:8000/api/vulns/vector-list/search/?version=2.0
http://127.0.0.1:8000/api/vulns/vector-list/search/?version=CVSSV3.1
"""
from django.urls import path, include

from apps.vulnerabilities.api import views

app_name = 'vulnerabilities'

urlpatterns = [
    path('cwe/<int:pk>/', views.CWEDetail.as_view(), name='cwe-detail'),
    path('cwe-list/', views.CWEView.as_view(), name='cwe-list'),

    path('cve-list/', views.CVEList.as_view(), name='cve-list'),
    path('cve/<int:pk>/', views.CVEDetail.as_view(), name='cve-detail'),
    path('cwe/<int:pk>/cve-create/', views.CVECreate.as_view(), name='cve-create'),
    path('cve-list/<str:cwe>/', views.CWECVEList.as_view(), name='cve-list-filter-cwe'),

    path('cpe-list/', views.CPEList.as_view(), name='cpe-list'),
    path('cpe/<int:pk>/', views.CPEDetail.as_view(), name='cpe-detail'),
    path('cve/<int:pk>/cpe-create/', views.CPECreate.as_view(), name='cpe-create'),

    path('reference-list/', views.ReferenceList.as_view(), name='reference-list'),
    path('reference/<int:pk>/', views.ReferenceDetail.as_view(), name='reference-detail'),
    path('cve/<int:pk>/reference-create/', views.ReferenceCreate.as_view(), name='reference-create'),

    path('vector-list/', views.VectorView.as_view(), name='vector-list'),
    path('vector-list/search/', views.VectorSearch.as_view(), name='vector-search'),
    path('vector-list/<str:severity>/', views.VectorSeverityList.as_view(), name='vector-list-filter-severity'),
    path('vector/<int:pk>/', views.VectorDetail.as_view(), name='vector-detail'),

]
