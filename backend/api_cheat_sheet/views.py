from django.shortcuts import render
from rest_framework import views
from urllib.request import urlopen
from bs4 import BeautifulSoup
from django.http import HttpResponse
from .models import CWEModel
from django.http import JsonResponse
from urllib.request import HTTPError
from django.db import IntegrityError
from django.http import HttpResponse, Http404


class Dowload_data(views.APIView):
    def data_url_database(request):
        for cwe_number in range(1,1253):
            definition=""
            try:
                print(cwe_number)
                url=urlopen('https://cwe.mitre.org/data/definitions/'+str(cwe_number)+".html").read()
                data_url=BeautifulSoup(url)
                definition_section=data_url.select('#Summary .detail .indent ')
                if not definition_section:
                    definition_section=data_url.select('#Description .detail .indent ')

                for element in definition_section:
                    definition=element.get_text()

                write_to_database = CWEModel.objects.create(number_cwe=cwe_number,definition=definition)

            except HTTPError as err:
                if err.code == 404:
                    continue
            except IntegrityError as e: 
                if 'unique constraint' in e.args:
                    continue 
                
        # informacja="wyświetlam informacje"
        # return HttpResponse("%s" %informacja)


class Written_from_database(views.APIView):
    def data_to_json(request, cwe_number):
        try:
            cwe = CWEModel.objects.get(number_cwe=cwe_number)
        except CWEModel.DoesNotExist:
            raise Http404("Invalid number")
        return JsonResponse({'cwe_code':cwe.code, 'definition':cwe.description})

