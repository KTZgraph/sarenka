"""
Source: https://gist.github.com/yehgdotnet/b9dfc618108d2f05845c4d8e28c5fc6a
"""

import mmh3
import requests
import codecs


class FaviconCalculator:
    @staticmethod
    def calculate(favicon_url):
        response = requests.get(favicon_url)
        # response = requests.get('https://cybersecurity.wtf/favicon.ico')
        favicon = codecs.encode(response.content, "base64")
        hash = mmh3.hash(favicon)
        return hash


if __name__ == "__main__":
    print(FaviconCalculator.calculate(""))

