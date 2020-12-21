"""
Obliczanie wartości Kryptograficznych Hashy.
Użycie biblioteki Crypto zamiast hashlib, ponieważ zawiera ona znane kolizje.

Nowoczesne algorytmy hashujące

rodzina SHA-2
    SHA-224
    SHA-256
    SHA-384
    SHA-512, SHA-512/224, SHA-512/256

rodzina SHA-3:
    SHA3-224
    SHA3-256
    SHA3-384
    SHA3-512

rodzaje BLAKE2
    BLAKE2s
    BLAKE2b
"""
from typing import Dict
import base64
from Crypto.Hash import SHA256, SHA224, SHA3_224, SHA3_256, SHA3_384,  SHA384, SHA512, BLAKE2s
import pprint


class CryptographicHashCalcualator:
    """
    Obliczanie wartości Kryptograficznych Hashy.
    Użycie biblioteki Crypto zamiast hashlib, ponieważ zawiera ona znane kolizje.
    """
    def __init__(self, user_value:str):
        self.original_value = user_value
        self.value = str.encode(user_value, "utf-8")

    @property
    def byte_string(self):
        return str.encode(self.value, "utf-8")

    def get_sha224(self):
        hash_obj = SHA224.new(data=self.value)
        return {
            "digest": hash_obj.digest(),
            "hexdigets": hash_obj.hexdigest()
        }

    def get_sha256(self):
        hash_obj = SHA256.new(data=self.value)
        return {
            "digest": hash_obj.digest(),
            "hexdigets": hash_obj.hexdigest()
        }

    def get_sha3_224(self):
        hash_obj = SHA3_224.new()
        hash_obj.update(self.value)
        return {
            "digest": hash_obj.digest(),
            "hexdigets": hash_obj.hexdigest()
        }

    def get_sha3_256(self):
        hash_obj = SHA3_256.new()
        hash_obj.update(self.value)
        return {
            "digest": hash_obj.digest(),
            "hexdigets": hash_obj.hexdigest()
        }

    def get_sha3_384(self):
        hash_obj = SHA3_384.new()
        hash_obj.update(self.value)
        return {
            "digest": hash_obj.digest(),
            "hexdigets": hash_obj.hexdigest()
        }

    def get_sha384(self):
        hash_obj = SHA384.new(data=self.value)
        return {
            "digest": hash_obj.digest(),
            "hexdigets": hash_obj.hexdigest()
        }

    def get_sha512(self):
        """
        UWAGA: Hash podanty na atak "length extension attack"
        http://netifera.com/research/flickr_api_signature_forgery.pdf
        you are able to compute h(m||pad(m)||m') for any m' (|| stands for concatenation), even if
        you don't know the entire message m
        https://crypto.stackexchange.com/questions/3978/understanding-the-length-extension-attack

        :return:
        """
        hash_obj = SHA512.new(data=self.value)
        return {
            "digest": hash_obj.digest(),
            "hexdigets": hash_obj.hexdigest(),
            "warning": "WARNING: SHA512 is vulnerable for length extension attack"
        }

    def get_sha512_truncate_224(self):
        hash_obj = SHA512.new(truncate="224")
        hash_obj.update(self.value)
        return {
            "digest": hash_obj.digest(),
            "hexdigets": hash_obj.hexdigest(),
            "warning": "WARNING: SHA512 is vulnerable for length extension attack"
        }

    def get_sha512_truncate_256(self):
        hash_obj = SHA512.new(truncate="256")
        hash_obj.update(self.value)
        return {
            "digest": hash_obj.digest(),
            "hexdigets": hash_obj.hexdigest(),
            "warning": "WARNING: SHA512 is vulnerable for length extension attack"
        }


    def get_blake2s_256_bits(self):
        """
        Weilkość digest_bits od 8 do 256
        The algorithm uses 32 bit words, and it therefore works best on 32-bit platforms. The digest size ranges from 8 to 256 bits:
        """
        hash_obj = BLAKE2s.new(digest_bits=256)
        hash_obj.update(self.value)
        return {
            "digest": hash_obj.digest(),
            "hexdigets": hash_obj.hexdigest()
        }

    def get_blake2s_as_mac(self, secret="secret"):
        # TODO: udsotępnić userowi dopisanie sekretnego klucza
        """
        Ewentulanie BLAKE2s może być użyty jak kryptograficzny MAC jeśli się zainicjalizuje go dodatkową  sekretną wartością
        :return:
        """
        mac = BLAKE2s.new(digest_bits=128, key=str.encode(secret))
        mac.update(self.value)
        return mac.digest(), mac.hexdigest()


class CryptographicHashWrapper: #TODO: refaktor - powtarzanie kodu
    """Wrapper na dane z CryptographicHashCalcualator ponieważ wystepują problemy z kodowaniem.
    Pomocnicza klasa zamiast serializera dla widoku"""
    def __init__(self, value:str):
        self.value = value.encode("utf-8")
        self.crypto_hash_calc = CryptographicHashCalcualator(value)

    def __convert_digest(self, digest):
        return base64.b64encode(digest)

    # sha224
    @property
    def sha224_digest(self):
        digest = self.crypto_hash_calc.get_sha224()["digest"]
        return self.__convert_digest(digest)

    @property
    def sha224_hexdigets(self):
        return self.crypto_hash_calc.get_sha224()["hexdigets"]

    # sha256
    @property
    def sha256_digest(self):
        digest = self.crypto_hash_calc.get_sha256()["digest"]
        return self.__convert_digest(digest)

    @property
    def sha256_hexdigets(self):
        return self.crypto_hash_calc.get_sha256()["hexdigets"]

    #sha3_224
    @property
    def sha3_224_digest(self):
        digest = self.crypto_hash_calc.get_sha3_224()["digest"]
        return self.__convert_digest(digest)

    @property
    def sha3_224_hexdigets(self):
        return self.crypto_hash_calc.get_sha3_224()["hexdigets"]

    #sha3_256
    @property
    def sha3_256_digest(self):
        digest = self.crypto_hash_calc.get_sha3_256()["digest"]
        return self.__convert_digest(digest)

    @property
    def sha3_256_hexdigets(self):
        return self.crypto_hash_calc.get_sha3_256()["hexdigets"]

    #sha3_384
    @property
    def sha3_384_digest(self):
        digest = self.crypto_hash_calc.get_sha3_384()["digest"]
        return self.__convert_digest(digest)

    @property
    def sha3_384_hexdigets(self):
        return self.crypto_hash_calc.get_sha3_384()["hexdigets"]

    #sha384
    @property
    def sha384_digest(self):
        digest = self.crypto_hash_calc.get_sha384()["digest"]
        return self.__convert_digest(digest)

    @property
    def sha384_hexdigets(self):
        return self.crypto_hash_calc.get_sha384()["hexdigets"]

    #sha512
    @property
    def sha512_digest(self):
        digest = self.crypto_hash_calc.get_sha512()["digest"]
        return self.__convert_digest(digest)

    @property
    def sha512_hexdigets(self):
        return self.crypto_hash_calc.get_sha512()["hexdigets"]

    @property
    def sha512_warning(self):
        return self.crypto_hash_calc.get_sha512()["warning"]

    # sha512_truncate_224
    @property
    def sha512_truncate_224_digest(self):
        digest = self.crypto_hash_calc.get_sha512_truncate_224()["digest"]
        return self.__convert_digest(digest)

    @property
    def sha512_truncate_224_hexdigets(self):
        return self.crypto_hash_calc.get_sha512_truncate_224()["hexdigets"]

    @property
    def sha512_truncate_224_warning(self):
        return self.crypto_hash_calc.get_sha512_truncate_224()["warning"]

    # sha512_truncate_256
    @property
    def sha512_truncate_256_digest(self):
        digest = self.crypto_hash_calc.get_sha512_truncate_256()["digest"]
        return self.__convert_digest(digest)

    @property
    def sha512_truncate_256_hexdigets(self):
        return self.crypto_hash_calc.get_sha512_truncate_256()["hexdigets"]

    @property
    def sha512_truncate_256_warning(self):
        return self.crypto_hash_calc.get_sha512_truncate_256()["warning"]

    # blake2s_256_bits
    @property
    def blake2s_256_bits_digest(self):
        digest = self.crypto_hash_calc.get_blake2s_256_bits()["digest"]
        return self.__convert_digest(digest)

    @property
    def blake2s_256_bits_hexdigets(self):
        return self.crypto_hash_calc.get_blake2s_256_bits()["hexdigets"]

    @property
    def values(self)->Dict:
        """Zwraca jsona który może być zwrócocny bezpoeśrednio przez widok Django."""
        return {
            # sha224
            "sha224_digest": self.sha224_digest,
            "sha224_hexdigets": str(self.sha224_hexdigets),

            # sha256
            "sha256_digest": self.sha256_digest,
            "sha256_hexdigets": self.sha256_hexdigets,

            # sha3_224
            "sha3_224_digest": self.sha3_224_digest,
            "sha3_224_hexdigets": self.sha3_224_hexdigets,

            # sha3_256
            "sha3_256_digest": self.sha3_256_digest,
            "sha3_256_hexdigets": self.sha3_256_hexdigets,

            # sha3_384
            "sha3_384_digest": self.sha3_384_digest,
            "sha3_384_hexdigets": self.sha3_384_hexdigets,

            # sha384
            "sha384_digest": self.sha384_digest,
            "sha384_hexdigets": self.sha384_hexdigets,

            # sha512
            "sha512_digest": self.sha512_digest,
            "sha512_hexdigets": self.sha512_hexdigets,
            "sha512_warning": self.sha512_warning,

            # sha512_truncate_224
            "sha512_truncate_224_digest": self.sha512_truncate_224_digest,
            "sha512_truncate_224_hexdigets": self.sha512_truncate_224_hexdigets,
            "sha512_truncate_224_warning": self.sha512_truncate_224_warning,

            # sha512_truncate_256
            "sha512_truncate_256_digest": self.sha512_truncate_256_digest,
            "sha512_truncate_256_hexdigets": self.sha512_truncate_256_hexdigets,
            "sha512_truncate_256_warning": self.sha512_truncate_256_warning,

            # blake2s_256_bits
            "blake2s_256_bits_digest": self.blake2s_256_bits_digest,
            "blake2s_256_bits_hexdigets": self.blake2s_256_bits_hexdigets
        }



if __name__ == "__main__":
    pprint.pprint(CryptographicHashCalcualator("Ala%20ma%20kota").get_data())
