"""
source: https://sector035.nl/articles/2020-50
"""

import requests
import re

from provider_url import ProviderUrl


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
    def parse_response(response_txt: str, user: str) -> dict:
        info, pub, uid = [None]*3
        response_txt = [i.rstrip() for i in response_txt.split('\n')]
        for r in response_txt:
            if 'info' in r:
                info = r.split('info:')[-1]
            if 'pub' in r:
                pub = r.split('pub:')[-1]
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
            print()
            response = Protonmail.get_response(user)
            if response:
                result.append(response)

        return result


if __name__ == "__main__":
    # res = Protonmail.get('admin')
    # print(res)
    # res = Protonmail.get('admin@protonmail.com')
    # print(res)
    res = Protonmail.get('renren')
    print(res)
