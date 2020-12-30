from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status


class CrtShView(APIView):
    service = "https://crt.sh"
    repository = "https://github.com/crtsh/certwatch_db"

    def get(self, identity):
        """
        Identity (Domain Name, Organization Name, etc),
        a Certificate Fingerprint (SHA-1 or SHA-256) or a crt.sh ID:
        """
        url = f"{CrtShView.service}/?q={identity}"
        # https://crt.sh/?q=google.pl
        return JsonResponse({"CrtSh" : "Not implemented yet"}, status=status.HTTP_501_NOT_IMPLEMENTED)