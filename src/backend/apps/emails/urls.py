from django.urls import path

from .views import ProtonmailAPIView

urlpatterns = [
    path('protonmail/<str:username>', ProtonmailAPIView.as_view(), name='protonmail'),
]
