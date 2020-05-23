
from django.urls import path
from searcher.views import CVESearchView
from searcher.views import Test_Class




urlpatterns = [
    path('cve/<str:code>', CVESearchView.as_view(), name="get_by_cve"),
    path('<int:test_id>/test/', Test_Class.ViewName, name='my_custom_sql'),

]