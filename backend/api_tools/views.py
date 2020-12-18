from rest_framework import views
from rest_framework.response import Response
import ipaddress
import socket

from .hash_calculator.cryptographic_hash_calculator import CryptographicHashWrapper as CryptoHash
from .hash_calculator.historic_hash_calculator import HistoricHashWrapper as HistoryHash
from .entropy_calculator.shanon_entropy import ShanonEntropy
from .port_scanner import PortScanner


class HashCalcualtorView(views.APIView):
    """Obliczanie najpopularnieszjych wartości hashy dla podanego ciagu znaków."""
    def get(self, request, value):
        """
        Zwraca wartości różnych hashy na podstawie stringa poganego przez użytkownika.
        """
        return Response({
            "cryptographic_hashes": CryptoHash(value).values,
            "historic_hashes": HistoryHash(value).values
        })


class EntropyCalculatorView(views.APIView):
    """Obliczanie Entropii ciągu znaków - obliczanie na podstawie entropi Shannona."""
    def get(self, request, value_sequence):

        return Response({
            "shanon_entropy": ShanonEntropy.calculate(value_sequence)
        })


class PortScannerView(views.APIView):
    """Uwaga - takie skanowanie zajmuje dużo czasu - zdecydowanie lepiej użyć oryginalnego nmapa!"""
    def is_ipv4(self, host):
        try:
            ipaddress.IPv4Network(host)
            return True
        except ValueError:
            return False

    def change_to_domain_addres(self, host):
        if self.is_ipv4(host):
            return host
        return socket.gethostbyname(host)

    def get(self, request, host, port):
        """
        Podstawowe skanowanie portów hosta.
        :param request: obiekt request django
        :param host: adres ip lub domeny wybranego hosta
        :return: informacje o statusie przeskanowanych portów - "open" albo "closed"
        """
        ip_address = self.change_to_domain_addres(host)

        try:
            return Response({
                "port_scanner": PortScanner(ip_address, port).scan()
            })
        except BaseException as e:
            print(e)
            print(type(e))
            return Response({
                "PortScanner": f"Unable to scan host={host}"
            })