from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse


@api_view(http_method_names=["GET"])  # żeby jako post endpoint traktował
def index(request) -> Response:
    return Response({"status": "success", "info": "ENGINES index."}, status=200)
