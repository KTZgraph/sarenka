from django.urls import path
from .views import HashCalcualtorView

urlpatterns = [
    path('hash_calculator/<str:value>', HashCalcualtorView.as_view(), name="hash_calculator"),
]
