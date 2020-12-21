"""
Moduł do obliczania entropii - rozbudowanie w przyszłosci
"""
import collections
from scipy.stats import entropy


class ShanonEntropy:
    @staticmethod
    def calculate(value_sequence:str):
        bases = collections.Counter([tmp_base for tmp_base in value_sequence])
        # define distribution
        dist = [x / sum(bases.values()) for x in bases.values()]

        # use scipy to calculate entropy
        entropy_value = entropy(dist, base=2)

        return entropy_value