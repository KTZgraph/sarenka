from rest_framework import APIView
from rest_framework.response import Response

# https://www.django-rest-framework.org/api-guide/status-codes/
from rest_framework import permissions, status


class RegisterView(APIView):
    def post(self, request):
        data = request.data

        return Response({}, status=status.HTTP_201_CREATED)


class RetrieveUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        pass
