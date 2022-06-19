from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..maintenance.maintenance import main


@api_view(http_method_names=['GET'])
def hello(request):
    return Response(
        {"status": "success", "info": "hello"}, status=200
    )

@api_view(http_method_names=['GET'])
def maintenance(request):
    try:
        main()
    except Exception as e:
        print(e)
        print(type(e))
        return Response(
        {"msg": str(e), "type": str(type(e))}, status=500)

    return Response(
        {"status": "success", "info": "maintenace"}, status=200
    )

