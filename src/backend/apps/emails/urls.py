from django.urls import path

from .views import ProtonmailAPIView, ProtonmailVPNAPIView

urlpatterns = [
    path('protonmail/<str:username>', ProtonmailAPIView.as_view(), name='protonmail'),
    path('protonmailvpn', ProtonmailVPNAPIView.as_view(), name='protonmail_vpn'),
]
