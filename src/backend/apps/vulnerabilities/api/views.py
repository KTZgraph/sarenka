from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(http_method_names=['GET'])
def hello(request):
    return Response(
        {"status": "success", "info": "hello"}, status=200
    )

@api_view(http_method_names=['GET'])
def maintenance(request):
    start = 0
    end = 0
    return Response(
        {"status": "success", "info": "maintenace", 'time': str(end-start)}, status=200
    )

