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

    @property
    def bytearray_value(self):
        return bytearray(self.value)

    def get_sha224(self):
        hash_obj = SHA224.new(data=self.value)
        print("Biciki: ",hash_obj.digest() )
        return {
            "digest": base64.b64encode(hash_obj.digest()),
            "hexdigets": str(hash_obj.hexdigest())
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

    def get_data(self):
        return {
            "sha224": self.get_sha224(),
            # "sha256": self.get_sha256(),
            # "sha3_224": self.get_sha3_224(),
            # "sha3_256": self.get_sha3_256(),
            # "sha3_384": self.get_sha3_384(),
            # "sha384": self.get_sha384(),
            # "sha512": self.get_sha512(),
            # "sha512_truncate_224": self.get_sha512_truncate_224(),
            # "sha512_truncate_256": self.get_sha512_truncate_256(),
            # "blake2s_256_bits": self.get_blake2s_256_bits(),


            # "get_blake2s_as_mac": self.get_blake2s_as_mac() #TODO
        }


if __name__ == "__main__":
    pprint.pprint(CryptographicHashCalcualator("Ala%20ma%20kota").get_data())
