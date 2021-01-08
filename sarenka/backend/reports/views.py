from fpdf import FPDF, HTMLMixin

import logging
from rest_framework.response import Response

from rest_framework import views


class GeneratePdf(views.APIView):
    def get(self, request, ip_address): #TODO: przepisać
        # pdf = PDF()
        # pdf.alias_nb_pages()
        # pdf.add_page()
        # ipAdress=ip_address
        # link="http://127.0.0.1:8000/search/censys/"
        # pdf.headerOnlyFirstSide(ipAdress)
        #
        #
        # try:
        #     pdf.chapter(ipAdress,link)
        # except (JSONDecodeError ,HTTPError) as e :
        #     return HttpResponse("Something went wrong. Check the ip address and your api key." )
        #
        #
        # else:
        #     pdf.set_font('Times', '', 12)
        #     pdf.output('reports/report_host_info.pdf', 'F')
        #     return FileResponse(open('reports/report_host_info.pdf', 'rb'))
        return Response({"error": "Not implemented yet"})
