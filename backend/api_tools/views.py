from rest_framework import views
from rest_framework.response import Response

from .hash_calculator.cryptographic_hash_calculator import CryptographicHashWrapper as CryptoHash
from .hash_calculator.historic_hash_calculator import HistoricHashWrapper as HistoryHash
from .entropy_calculator.shanon_entropy import ShanonEntropy


class HashCalcualtorView(views.APIView):
    def get(self, request, value):
        """
        Zwraca wartości różnych hashy na podstawie stringa poganego przez użytkownika.
        """
        return Response({
            "cryptographic_hashes": CryptoHash(value).values,
            "historic_hashes": HistoryHash(value).values
        })


class EntropyCalculatorView(views.APIView):
    def get(self, request, value_sequence):

        return Response({
            "shanon_entropy": ShanonEntropy.calculate(value_sequence)
        })