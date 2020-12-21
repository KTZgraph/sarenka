"""
Kalkulator historycznych algorytmów hashujących - NIE używac w kryptografi.

SHA-1
MD2
MD5
RIPEMD-160
Keccak
"""
from typing import Dict
from Crypto.Hash import SHA1, MD2, MD5, RIPEMD160, keccak
import base64

class HistoricHashCalcualator:
    """
    Obliczanie wartości Kryptograficznych Hsitorycznych Hashy.
    Użycie biblioteki Crypto zamiast hashlib, ponieważ zawiera ona znane kolizje.
    """
    def __init__(self, user_value:str):
        self.original_value = user_value
        self.value = str.encode(user_value, "utf-8")

    def get_sha1(self):
        hash_obj = SHA1.new()
        hash_obj.update(self.value)
        return {
            "digest": hash_obj.digest(),
            "hexdigets": hash_obj.hexdigest(),
            "warning": "WARNING: Insecure and vulnerable to length-extension attacks."
        }

    def get_md2(self):
        hash_obj = MD2.new()
        hash_obj.update(self.value)
        return {
            "digest": hash_obj.digest(),
            "hexdigets": hash_obj.hexdigest(),
            "warning": "WARNING: Insecure."
        }

    def get_md5(self):
        hash_obj = MD5.new()
        hash_obj.update(self.value)
        return {
            "digest": hash_obj.digest(),
            "hexdigets": hash_obj.hexdigest(),
            "warning": "WARNING: Insecure and vulnerable to length-extension attacks."
        }

    def get_ripemd160(self):
        hash_obj = RIPEMD160.new()
        hash_obj.update(self.value)
        return {
            "digest": hash_obj.digest(),
            "hexdigets": hash_obj.hexdigest(),
            "warning": "WARNING: Insecure and vulnerable to length-extension attacks."
        }

    # keccak
    def get_keccak_224_bits(self):
        hash_obj = keccak.new(digest_bits=224)
        hash_obj.update(self.value)
        return {
            "digest": hash_obj.digest(),
            "hexdigets": hash_obj.hexdigest(),
        }

    def get_keccak_256_bits(self):
        hash_obj = keccak.new(digest_bits=256)
        hash_obj.update(self.value)
        return {
            "digest": hash_obj.digest(),
            "hexdigets": hash_obj.hexdigest(),
        }

    def get_keccak_384_bits(self):
        hash_obj = keccak.new(digest_bits=384)
        hash_obj.update(self.value)
        return {
            "digest": hash_obj.digest(),
            "hexdigets": hash_obj.hexdigest(),
        }

    def get_keccak_512_bits(self):
        hash_obj = keccak.new(digest_bits=512)
        hash_obj.update(self.value)
        return {
            "digest": hash_obj.digest(),
            "hexdigets": hash_obj.hexdigest(),
        }


class HistoricHashWrapper:
    """Wrapper na dane z HistoricHashCalcualator ponieważ wystepują problemy z kodowaniem.
    Pomocnicza klasa zamiast serializera dla widoku"""
    def __init__(self, value:str):
        self.value = value.encode("utf-8")
        self.hash_calc = HistoricHashCalcualator(value)

    def __convert_digest(self, digest):
        return base64.b64encode(digest)

    # sha1
    @property
    def sha1_digest(self):
        digest = self.hash_calc.get_sha1()["digest"]
        return self.__convert_digest(digest)

    @property
    def sha1_hexdigets(self):
        return self.hash_calc.get_sha1()["hexdigets"]

    @property
    def sha1_warning(self):
        return self.hash_calc.get_sha1()["warning"]

    # md2
    @property
    def md2_digest(self):
        digest = self.hash_calc.get_md2()["digest"]
        return self.__convert_digest(digest)

    @property
    def md2_hexdigets(self):
        return self.hash_calc.get_md2()["hexdigets"]

    @property
    def md2_warning(self):
        return self.hash_calc.get_md2()["warning"]

    # md5
    @property
    def md5_digest(self):
        digest = self.hash_calc.get_md5()["digest"]
        return self.__convert_digest(digest)

    @property
    def md5_hexdigets(self):
        return self.hash_calc.get_md5()["hexdigets"]

    @property
    def md5_warning(self):
        return self.hash_calc.get_md5()["warning"]

    # ripemd160
    @property
    def ripemd160_digest(self):
        digest = self.hash_calc.get_ripemd160()["digest"]
        return self.__convert_digest(digest)

    @property
    def ripemd160_hexdigets(self):
        return self.hash_calc.get_ripemd160()["hexdigets"]

    @property
    def ripemd160_warning(self):
        return self.hash_calc.get_ripemd160()["warning"]

    ##### keccak
    # keccak_224_bits
    @property
    def keccak_224_bits_digest(self):
        digest = self.hash_calc.get_keccak_224_bits()["digest"]
        return self.__convert_digest(digest)

    @property
    def keccak_224_bits_hexdigets(self):
        return self.hash_calc.get_keccak_224_bits()["hexdigets"]

    # keccak_256_bits
    @property
    def keccak_256_bits_digest(self):
        digest = self.hash_calc.get_keccak_256_bits()["digest"]
        return self.__convert_digest(digest)

    @property
    def keccak_256_bits_hexdigets(self):
        return self.hash_calc.get_keccak_256_bits()["hexdigets"]

    # keccak_384_bits
    @property
    def keccak_384_bits_digest(self):
        digest = self.hash_calc.get_keccak_384_bits()["digest"]
        return self.__convert_digest(digest)

    @property
    def keccak_384_bits_hexdigets(self):
        return self.hash_calc.get_keccak_384_bits()["hexdigets"]

    # get_keccak_512_bits
    @property
    def keccak_512_bits_digest(self):
        digest = self.hash_calc.get_keccak_512_bits()["digest"]
        return self.__convert_digest(digest)

    @property
    def keccak_512_bits_hexdigets(self):
        return self.hash_calc.get_keccak_512_bits()["hexdigets"]

    @property
    def values(self)->Dict:
        """Zwraca jsona który może być zwrócocny bezpoeśrednio przez widok Django."""
        return {
            # sha1
            "sha1_digest": self.sha1_digest,
            "sha1_hexdigets": self.sha1_hexdigets,
            "sha1_warning": self.sha1_warning,

            # md2
            "md2_digest": self.md2_digest,
            "md2_hexdigets": self.md2_hexdigets,
            "md2_warning": self.md2_warning,

            # md5
            "md5_digest": self.md5_digest,
            "md5_hexdigets": self.md5_hexdigets,
            "md5_warning": self.md5_warning,

            # ripemd160
            "ripemd160_digest": self.ripemd160_digest,
            "ripemd160_hexdigets": self.ripemd160_hexdigets,
            "ripemd160_warning":self.ripemd160_warning,

            # keccak_224_bits
            "keccak_224_bits_digest": self.keccak_224_bits_digest,
            "keccak_224_bits_hexdigets": self.keccak_224_bits_hexdigets,

            # keccak_256_bits
            "keccak_256_bits_digest": self.keccak_256_bits_digest,
            "keccak_256_bits_hexdigets": self.keccak_256_bits_hexdigets,

            # keccak_384_bits
            "keccak_384_bits_digest": self.keccak_384_bits_digest,
            "keccak_384_bits_hexdigets": self.keccak_384_bits_hexdigets,

            # get_keccak_512_bits
            "keccak_512_bits_digest": self.keccak_512_bits_digest,
            "keccak_512_bits_hexdigets": self.keccak_512_bits_hexdigets
        }
