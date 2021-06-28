from django.urls import path, include

from apps.vulnerabilities.api import views

app_name = 'vulnerabilities'

urlpatterns = [
    path('cwes/', views.CWEView.as_view(), name='cwe-list'),
    # path('cves/', CVEGenericAPIView.as_view()),
    # path('cves/<str:pk>/', CVEGenericAPIView.as_view()),
    # path('cwes/', CWEGenericAPIView.as_view()),
    # path('cwes/<str:pk>/', CWEGenericAPIView.as_view()),
]
