from rest_framework import views, status
from rest_framework.response import Response
import sys

from api_searcher.windows.hardware import Hardware
from api_searcher.windows.local import LocalInfo
from api_searcher.windows.network import LocalNetworkData
from api_searcher.windows.registry import WindowsRegistry


def is_windows_os():
    return sys.platform.startswith('win')


class NetworkLocalView(views.APIView):
    """Widok Django zwracający informacje o lokalnej sieci na podstawie danych dostępnych w systemie Windows."""

    def get(self, request):
        """
        Zwraca informacje sieciowe lokalnej maszyny na której uruchomiono serwer aplikacji
        na podstawie żądania GET HTTP użytkownika.
        :param request: obiekt dla widoku Django z informacjami od użytkownika
        :return: dane w postaci json zawierajace informacje o sieci w jakiej znajduje się host
        """
        if is_windows_os():
            try:
                return Response(LocalNetworkData().values)
            except BaseException as ex:
                return Response(
                    {"error": "Unable to get network information.", "details": str(ex)},
                    status=status.HTTP_501_NOT_IMPLEMENTED)
        else:
            return Response({"message": "Method not allowed on this OS."},
                            status=status.HTTP_417_EXPECTATION_FAILED)


class LocalView(views.APIView):
    """Widok Django zwracajacy informacje o lokalnej maszynie Windows"""
    def get(self, request):
        """
        Zwraca ogólne informacje o lokalnej maszynie na której uruchomiono serwer aplikacji
        na podstawie żądania GET HTTP użytkownika.
        :param request: obiekt dla widoku Django z informacjami od użytkownika
        :return: dane w postaci json zawierajace ogólne informacje o maszynie na której uruchomiono aplikacje
        """
        if is_windows_os():
            try:
                return Response(LocalInfo().values)
            except Exception as ex:
                return Response(
                    {"error": "Unable to get general Windows machine information.", "details": str(ex)},
                    status=status.HTTP_501_NOT_IMPLEMENTED)
        else:
            return Response({"message": "Method not allowed on this OS."},
                            status=status.HTTP_417_EXPECTATION_FAILED)


class HardwareView(views.APIView):
    """Widok zwracajacy informacje sprzętowe dostępne z poziomu systemu Windows"""

    def get(self, request):
        """Zwraca informacje sprzętowe o lokalnej maszynie na której uruchomiono serwer aplikacji
        na podstawie żądania GET HTTP użytkownika.
        :param request: obiekt dla widoku Django z informacjami od użytkownika
        :return: dane w postaci json zawierajace informacje sprzętowe
        """
        if is_windows_os():
            try:
                hardware = Hardware()
                response = hardware.to_json()
                return Response(response)
            except BaseException as ex:
                return Response(
                    {"error": "Unable to get Windows hardware data.", "details": str(ex)},
                    status=status.HTTP_501_NOT_IMPLEMENTED
                )
        else:
            return Response({"message": "Method not allowed on this OS."}, status=status.HTTP_417_EXPECTATION_FAILED)


class RegistryView(views.APIView):
    """Widok Django zwracający informacje o lokalnie zainstalowanym oprogramowaniu w systemie Windows"""
    def get(self, request):
        """
        Zwraca informacje o lokalnie zainstalowanym oprogramowaniu w systemie Windows na podstawie żądania GET HTTP użytkownika.
        :param request: obiekt dla widoku Django z informacjami od użytkownika
        :return: dane w postaci json zawierajace informacje o lokalnych aplikacjach
        """
        if is_windows_os():
            try:
                windows_registry = WindowsRegistry()
                response = windows_registry.get_all_software()
                return Response(response)
            except BaseException as ex:
                return Response(
                    {"error": "Unable to get data from Windows registry", "details": str(ex)},
                    status=status.HTTP_501_NOT_IMPLEMENTED
                )
        else:
            return Response({"message": "Method not allowed on this OS."}, status=status.HTTP_417_EXPECTATION_FAILED)