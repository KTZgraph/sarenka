
from django.urls import path
from analyzer_api.views import ImageMagickFileView, ImageMagickListView, ImageMagickUrlView, LocalWindows

urlpatterns = [
    path('imagemagick/file/', ImageMagickFileView.as_view(), name="get_imagemagick_file"),
    path('imagemagick/list/', ImageMagickListView.as_view(), name="get_imagemagick_list"),
    path('imagemagick/url/', ImageMagickUrlView.as_view(), name="get_imagemagick_url"),
    path('local/windows/', LocalWindows.as_view(), name="local_windows")
]
