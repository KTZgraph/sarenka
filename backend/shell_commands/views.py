from django.shortcuts import render
# from django.shortcuts import render
from rest_framework import views
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# from django.http import HttpResponse
# from .models import Knowledge_base
from django.http import JsonResponse
# from urllib.request  import HTTPError
# from django.db import IntegrityError
# from django.http import HttpResponse, Http404
# Create your views here.
import subprocess


class commands(views.APIView):
    def get_smbiosversiob(request):     
        # # value = "ddd"
        # try:
        value = subprocess.run("wmic bios get smbiosbiosversion")
        # except Knowledge_base.DoesNotExist:
        #     raise Http404("Invalid number")
        return value
        # subprocess.call(["wmic bios get smbiosversiob", "-1"], shell=True)