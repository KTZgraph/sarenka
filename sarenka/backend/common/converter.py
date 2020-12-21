import json
from typing import List, Dict

class Converter:
    """Most common conversion operations"""

    @staticmethod
    def json_to_dict(data)->Dict:
        """Takes json file and return python dictionary"""
        print(data)
        print(type(data))

    @staticmethod
    def flatten_list(l:List)->List:
        """Python trick to make the list flat"""
        return sum(l, [])

    @staticmethod
    def dict_sort(d:Dict)->Dict:
        pass

    @staticmethod
    def remove_duplicates(l:List)->List:
        """Removes duplicates and sort list"""
        s = set(l)
        l = list(s)
        l.sort()
        return l