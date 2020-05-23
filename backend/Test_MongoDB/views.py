from django.shortcuts import render
from rest_framework import views
from .models import Test_mongo
from django.http import HttpResponse
import pyrebase
# Create your views here.

config = {
  'apiKey': "AIzaSyC7q83jVJJN5VRQqMJyEzd-XYUkUMp6EBw",
  'authDomain': "base-firebase-77930.firebaseapp.com",
  'databaseURL': "https://base-firebase-77930.firebaseio.com",
  'projectId': "base-firebase-77930",
  'storageBucket': "base-firebase-77930.appspot.com",
  'messagingSenderId': "46510538835",
  'appId': "1:46510538835:web:3b825b550d6e1192c506a6"
};
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
class Test_Class_MongoDB(views.APIView):
    
    def  ViewName_MongoDB(request, test_id):
        text2 = Test_mongo.objects.get(pk=test_id)
        return HttpResponse("%s" %text2 )


class Test_Class_firebase(views.APIView):
    
    def  ViewName_firebase(request, test_id):
        text2 = Test_mongo.objects.get(pk=test_id)
        return HttpResponse("%s" %text2 )