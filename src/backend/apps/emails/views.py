from rest_framework.response import Response
from rest_framework import views

from .providers.protonmail import Protonmail


class ProtonmailAPIView(views.APIView):
    def get(self, request, username):
        return Response({
            'data': Protonmail.get(username)
        })

