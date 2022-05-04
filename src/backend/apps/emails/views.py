from rest_framework.response import Response
from rest_framework import views

from .providers.protonmail import Protonmail, ProtonmailVPN


class ProtonmailVPNAPIView(views.APIView):
    def get(self, request):
        return Response({"data": ProtonmailVPN.get()})


class ProtonmailAPIView(views.APIView):
    def get(self, request, username):
        return Response({"data": Protonmail.get(username)})
