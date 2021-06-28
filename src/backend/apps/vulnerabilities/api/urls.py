from django.urls import path, include

from apps.vulnerabilities.api import views

app_name = 'vulnerabilities'

urlpatterns = [
    path('cwe/<int:pk>/', views.CWEDetail.as_view(), name='cwe-detail'),
    path('cwe-list/', views.CWEView.as_view(), name='cwe-list'),

    path('cve-list/', views.CVEList.as_view(), name='cve-list'),
    path('cwe/<int:pk>/cve-create/', views.CVECreate.as_view(), name='cve-create'),
    path('cve/<int:pk>/', views.CVEDetail.as_view(), name='cve-detail'),

    path('cve/<int:pk>/cpe-create/', views.CPECreate.as_view(), name='cpe-create'),
    path('cpe-list/', views.CPEList.as_view(), name='cpe-list'),


    path('vector-list/', views.VectorView.as_view(), name='vector-list'),
    path('reference-list/', views.ReferenceView.as_view(), name='reference-list'),
]
