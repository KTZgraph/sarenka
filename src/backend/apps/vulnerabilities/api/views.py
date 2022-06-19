from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..maintenance.cwe import main as cwe_maintenance
from ..maintenance.cve import main as cve_main

@api_view(http_method_names=['GET'])
def hello(request):
    return Response(
        {"status": "success", "info": "hello"}, status=200
    )

@api_view(http_method_names=['GET'])
def maintenance(request):
    try:
        cwe_maintenance()
    except Exception as e:
        print(e)
        print(type(e))
        return Response(
        {"msg": str(e), "type": str(type(e))}, status=500)

    try:
        cve_main()
    except Exception as e:
        print(e)
        print(type(e))
        return Response(
        {"function":"cve", "msg": str(e), "type": str(type(e))}, status=500)

    return Response(
        {"status": "success", "info": "maintenace"}, status=200
    )

