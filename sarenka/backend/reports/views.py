from fpdf import FPDF, HTMLMixin

import logging
from rest_framework.response import Response

from rest_framework import views
from reports.host_info import PDFHostInfo
from reports.hardware_info import PDFHardwareInfo

from json.decoder import JSONDecodeError
from urllib.error import HTTPError
from django.http import HttpResponse
from django.http import FileResponse


class GeneratePdfHostInfo(views.APIView):
    def get(self, request, ip_address): 
        pdf = PDFHostInfo()
        pdf.alias_nb_pages()
        pdf.add_page()
        link="http://127.0.0.1:8000/api/censys/"
        pdf.headerOnlyFirstSide(ip_address)
         
        try:
            pdf.chapter(ip_address,link)
        except (JSONDecodeError ,HTTPError) as e :
            return HttpResponse("Something went wrong. Check the ip address and your api key." )
        
        else:
            pdf.set_font('Times', '', 12)
            pdf.output('reports/report_host_info.pdf', 'F')
            return FileResponse(open('reports/report_host_info.pdf', 'rb'))

class GeneratePdfHardware(views.APIView):
    def get(self, request): 
        pdf = PDFHardwareInfo()
        pdf.alias_nb_pages()
        pdf.add_page()
        link="http://127.0.0.1:8000/api/local/hardware"
        pdf.headerOnlyFirstSide()
         
        try:
            pdf.chapter(link)
        except (JSONDecodeError ,HTTPError) as e :
            return HttpResponse("Something went wrong." )
        
        else:
            pdf.set_font('Times', '', 12)
            pdf.output('reports/report_hardware_info.pdf', 'F')
            return FileResponse(open('reports/report_hardware_info.pdf', 'rb'))

