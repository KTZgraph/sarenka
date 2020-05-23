
from django.urls import path
from Test_MongoDB.views import Test_Class_MongoDB

urlpatterns = [
    path('<int:test_id>/test_mongo/', Test_Class_MongoDB.ViewName_MongoDB, name='my_custom_sql'),

]