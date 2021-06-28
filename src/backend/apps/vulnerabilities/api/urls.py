from django.urls import path, include

from apps.vulnerabilities.api import views

app_name = 'vulnerabilities'

urlpatterns = [
    path('cwe/<int:pk>/', views.CWEDetail.as_view(), name='cwe-detail'),
    path('cwe-list/', views.CWEList.as_view(), name='cwe-list'),
    path('cve-list/', views.CVEView.as_view(), name='cve-list'),
    path('vector-list/', views.VectorView.as_view(), name='vector-list'),
    path('reference-list/', views.ReferenceView.as_view(), name='reference-list'),
    path('cpe-list/', views.CPEView.as_view(), name='cpe-list'),
]
