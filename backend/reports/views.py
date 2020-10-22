from fpdf import FPDF, HTMLMixin
import json
import requests
from connectors.credential import Credential
from connectors.cve_search.connector import Connector as CVEConnector
from connectors.censys.connector import Connector as CensysConnector
# from reports.host_info import PDF
from rest_framework import views
from rest_framework.response import Response
from django.http import HttpResponse
from django.http import FileResponse

from reports.host_info import PDF


class GeneratePdf(views.APIView):
    def get(self, request, ip_address):     
        pdf = PDF()
        pdf.alias_nb_pages()
        pdf.add_page()
        ipAdress="46.29.18.78"
        link="http://127.0.0.1:8000/search/censys/"
        pdf.headerOnlyFirstSide(ipAdress)
        pdf.chapter(ipAdress,link)
        pdf.set_font('Times', '', 12)
        pdf.output('reports/report_host_info.pdf', 'F')
        # response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        # return FileResponse(pdf.output('report_host_info.pdf', 'S'), content_type='application/pdf')
        return FileResponse(open('reports/report_host_info.pdf', 'rb'))
        # return Response(response.to_json)
        # return HttpResponse(return Response(response.to_json))