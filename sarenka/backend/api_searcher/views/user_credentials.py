from rest_framework import views, status
from rest_framework.response import Response

from api_searcher.serializers import UserCredentialsSerializer, CensysCredentailsSerializer, ShodanCredentailsSerializer
from api_searcher.search_engines.user_credentials import UserCredentials, UserCredentialsError
from api_searcher.search_engines.user_credentials_updater import UserCredentialsUpdater, UserCredentialsUpdaterError


class UserCredentialsView(views.APIView):
    serializer_class = UserCredentialsSerializer

    def get(self, request):
        try:
            user_credentials = UserCredentials()
            details = {
                "censys": {
                    "API_ID": user_credentials.censys.api_id,
                    "Secret": user_credentials.censys.secret,
                },
                "shodan": {
                    "user": user_credentials.shodan.user,
                    "api_key": user_credentials.shodan.api_key,
                }
            }

            return Response(details)
        except UserCredentialsError as ex:
            Response({"error": "Unable to get user credentials.", "details": str(ex)}, status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response({"error": "User credentials are not valid. Please chceck file "
                                      "user_credentials.sqlite3 database",
                             "details": str(ex)},
                            status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        """Zapisuje do bazy dane uwierzytelniające użytkownika do serwisów trzecich."""

        user_data = request.data
        print(user_data)
        try:
            details = {
                "censys": {
                    "API_ID": user_data.get("censys.api_id"),
                    "Secret":  user_data.get("censys.secret"),
                },
                "shodan": {
                    "user":  user_data.get("shodan.user"),
                    "api_key": user_data.get("shodan.api_key"),
                }
            }
            UserCredentialsUpdater(details).update()
            return Response({"message": "User credentials added.", "details": details})
        except UserCredentialsError as ex:
            Response({"error": "Invalid user credentials.", "details": str(ex)}, status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response({"error": "Unable to add user credentials.", "details": str(ex)}, status.HTTP_400_BAD_REQUEST)



