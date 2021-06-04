from django.urls import path

from .views import AtanerAPI

urlpatterns = [
    path('ziemniaczek/', AtanerAPI.as_view(), name='image_analyzer'),
]
