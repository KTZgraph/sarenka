from django.urls import path
from .views import HashCalcualtorView, EntropyCalculatorView, PortScannerView

urlpatterns = [
    path('hash/<str:value>', HashCalcualtorView.as_view(), name="hash_calculator"),
    path('entropy/<str:value_sequence>', EntropyCalculatorView.as_view(), name="entropy_calculator"),
    path('port_scanner/<str:host>/<str:port>/', PortScannerView.as_view(), name="port_scanner"),
]
