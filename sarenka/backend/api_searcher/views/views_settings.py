from rest_framework import views, status
from rest_framework.response import Response

from api_searcher.serializers import SettingsSerializer


class SettingsView(views.APIView):
    serializer_class = SettingsSerializer

    def post(self, request):
        """Tworzy plik z danymi użytkownika do serwisów trzecich."""
        serializer = SettingsSerializer(data=request.data)

        # walidacja danych
        if serializer.is_valid():
            details = {
                "censys_API_ID": serializer.data.get("censys_API_ID"),
                "censys_Secret": serializer.data.get("censys_Secret"),
                "shodan_user": serializer.data.get("shodan_user"),
                "shodan_api_key": serializer.data.get("shodan_api_key"),
            }

            return Response({"message": "Settings added.", "details": details})
        else:
            return Response({"message": "Given settings are not valid.", "details": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)