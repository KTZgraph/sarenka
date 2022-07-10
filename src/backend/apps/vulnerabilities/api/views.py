from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(http_method_names=['GET'])
def hello(request):
    return Response(
        {"status": "success", "info": "hello"}, status=200
    )

@api_view(http_method_names=['GET'])
def maintenance(request):
    return Response(
        {"status": "success", "info": "maintenace"}, status=200
    )

