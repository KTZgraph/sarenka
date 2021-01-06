from rest_framework import views, status
from rest_framework.response import Response

from api_searcher.serializers import UserCredentialsSerializer
from api_searcher.search_engines.user_credentials import UserCredentials, UserCredentialsError
from api_searcher.search_engines.user_credentials_updater import UserCredentialsUpdater, UserCredentialsUpdaterError


class UserCredentialsView(views.APIView):
    serializer_class = UserCredentialsSerializer

    def get(self, request):
        # Michałowi zrobić
        try:
            user_credentials = UserCredentials()
            response = {
                "censys_API_ID": user_credentials.censys.api_id,
                "censys_Secret": user_credentials.censys.secret,
                "shodan_user": user_credentials.shodan.user,
                "shodan_api_key": user_credentials.shodan.api_key,
            }
            return Response(response)
        except UserCredentialsError as ex:
            Response({"error": "Unable to get user credentials.", "details": str(ex)}, status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response({"error": "User credentials are not valid. Please chceck if file "
                                      "sarenka\\backend\\api_searcher\\search_engines\\user_credentials.json exists "
                                      "and is valid or copy from repository https://github.com/pawlaczyk/sarenka/",
                             "details": str(ex)},
                            status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        """Tworzy plik z danymi użytkownika do serwisów trzecich."""
        try:

            serializer = UserCredentialsSerializer(data=request.data)

            # walidacja danych
            if serializer.is_valid():
                details = {
                    "censys_API_ID": serializer.data.get("censys_API_ID"),
                    "censys_Secret": serializer.data.get("censys_Secret"),
                    "shodan_user": serializer.data.get("shodan_user"),
                    "shodan_api_key": serializer.data.get("shodan_api_key"),
                }
                UserCredentialsUpdater(details).update()
                return Response({"message": "User credentials added.", "details": details})
            else:
                return Response({"message": "User credentials are not valid.", "details": serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)

        except UserCredentialsUpdaterError as ex:
            return Response({"error": "Unable to update user credentials.", "details": str(ex)},
                                status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response({"error": "User credentials are not valid. Please chceck if file "
                                "sarenka\\backend\\api_searcher\\search_engines\\user_credentials.json exists "
                                "and is valid or copy from repository https://github.com/pawlaczyk/sarenka/",
                                "details": str(ex)},
                                status=status.HTTP_400_BAD_REQUEST)


