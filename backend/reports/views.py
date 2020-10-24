from fpdf import FPDF, HTMLMixin
import json
import requests

# from connectors.credential import Credential
# from connectors.cve_search.connector import Connector as CVEConnector
# from connectors.censys.connector import Connector as CensysConnector

from rest_framework import views
from django.http import FileResponse
from reports.host_info import PDF



class GeneratePdf(views.APIView):
    def get(self, request, ip_address):     
        pdf = PDF()
        pdf.alias_nb_pages()
        pdf.add_page()
        ipAdress=ip_address
        link="http://127.0.0.1:8000/search/censys/"
        pdf.headerOnlyFirstSide(ipAdress)
        pdf.chapter(ipAdress,link)
        pdf.set_font('Times', '', 12)
        pdf.output('reports/report_host_info.pdf', 'F')

        return FileResponse(open('reports/report_host_info.pdf', 'rb'))