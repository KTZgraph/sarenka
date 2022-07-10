from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.vulnerabilities.src.maintenance.vulns import save_db




@api_view(http_method_names=['GET'])
def hello(request):
    return Response(
        {"status": "success", "info": "hello"}, status=200
    )

@api_view(http_method_names=['GET'])
def maintenance(request):
    start = datetime.now()
    missed_cwe_ids = save_db()
    end = datetime.now()
    return Response(
        {"status": "success", "info": "maintenace", 'time': str(end-start), "missed_cwe_ids": missed_cwe_ids}, status=200
    )

