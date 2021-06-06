from django.urls import path

from .views import ProtonmailAPIView, ProtonmailVPNAPIView

app_name = 'emails'

urlpatterns = [
    path('protonmail/<str:username>', ProtonmailAPIView.as_view(), name='protonmail'),
    path('protonmailvpn', ProtonmailVPNAPIView.as_view(), name='protonmail_vpn'),
]
