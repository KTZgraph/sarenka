
from django.urls import path
from analyzer_api.views import ImageMagickFileView, ImageMagickListView, ImageMagickUrlView

urlpatterns = [
    path('imagemagick/file', ImageMagickFileView.as_view(), name="get_imagemagick_file"),
    path('imagemagick/list', ImageMagickListView.as_view(), name="get_imagemagick_list"),
    path('imagemagick/url', ImageMagickUrlView.as_view(), name="get_imagemagick_url"),
]
