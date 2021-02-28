from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import CVEGenericAPIView

urlpatterns = [
    path('cves', CVEGenericAPIView.as_view()),
    path('cves/<str:pk>', CVEGenericAPIView.as_view()),
    # path('upload', FileUploadView.as_view()),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]
