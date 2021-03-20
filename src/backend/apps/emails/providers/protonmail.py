"""
source: https://sector035.nl/articles/2020-50
"""

import requests
import re

from .provider_url import ProviderUrl


class ProtonmailVPN:
    @staticmethod
    def get() -> dict:
        response = requests.get(ProviderUrl().protonmail_vpn)
        return response.json()


class Protonmail:
    @staticmethod
    def get_user_email(username: str) -> list:
        if '@protonmail.com' in username or '@protonmail.ch' in username or '@pm.me' in username:
            return [username]
        else:
            return [f'{username}@protonmail.com', f'{username}@protonmail.ch', f'{username}@pm.me']

    @staticmethod
    def get_public_key(email: str):
        feed_ulr = f'{ProviderUrl().protonmail_pk}{email}'
        response = requests.get(feed_ulr).text
        return response

    @staticmethod
    def get_encryption_type(pub):
        if ':2048:' in pub:
            return 'rsa_2048'
        if ':4096:' in pub:
            return 'rsa_4096'
        if ':22::' in pub:
            return 'x25519'

        return 'Unable to obtain.'

    @staticmethod
    def parse_response(response_txt: str, user: str) -> dict:
        info, pub, uid, encryption = [None]*4
        response_txt = [i.rstrip() for i in response_txt.split('\n')]
        for r in response_txt:
            if 'info' in r:
                info = r.split('info:')[-1]
            if 'pub' in r:
                pub = r.split('pub:')[-1]
                encryption = Protonmail.get_encryption_type(pub)
            if 'uid' in r:
                uid = r.split('uid:')[-1]

        try:
            email = re.search(r'<(.*?)>', uid).group(1)
            email_pk = Protonmail.get_public_key(email)
        except (AttributeError, TypeError):
            email = None
            email_pk = None

        return {
            'info': 'valid' if '1:1' in info else 'invalid',
            'pub': pub,
            'uid': uid,
            'parsed_email': email,
            'checked_email': user,
            'encryption': encryption,
            'pk': email_pk
        }

    @staticmethod
    def get_response(user):
        feed_url = f'{ProviderUrl().protonmail}{user}'
        res_txt = requests.get(feed_url).text
        return Protonmail.parse_response(res_txt, user)

    @staticmethod
    def get(username: str):
        result = []
        usernames = Protonmail.get_user_email(username)
        for user in usernames:
            response = Protonmail.get_response(user)
            if response:
                result.append(response)

        return result


# if __name__ == "__main__":
#     ProtonmailVPN.get()
#     res = Protonmail.get('admin')
#     print(res)
#     res = Protonmail.get('admin@protonmail.com')
#     print(res)
#     res = Protonmail.get('renren')
#     print(res)
