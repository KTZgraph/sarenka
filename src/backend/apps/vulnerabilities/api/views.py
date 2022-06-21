from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..maintenance.cwe import main as main_cwe
from ..maintenance.cve import main as main_cve


@api_view(http_method_names=['GET'])
def hello(request):
    return Response(
        {"status": "success", "info": "hello"}, status=200
    )

@api_view(http_method_names=['GET'])
def maintenance(request):
    start = datetime.now()
    try:
        main_cwe()
        main_cve()
    except Exception as e:
        print(e)
        print(type(e))
        return Response(
        {"msg": str(e), "type": str(type(e))}, status=500)

    end = datetime.now()
    return Response(
        {"status": "success", "info": "maintenace", 'time': str(end-start)}, status=200
    )

