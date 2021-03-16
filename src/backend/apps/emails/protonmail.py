"""
source: https://sector035.nl/articles/2020-50
"""

import requests
import re


class Protonmail:
    _feed = "https://api.protonmail.ch/pks/lookup?op=index&search="

    @staticmethod
    def get_user_email(username: str) -> list:
        if '@protonmail.com' in username or '@protonmail.ch' in username:
            return [username]
        else:
            return [f'{username}@protonmail.com', f'{username}@protonmail.ch']

    @staticmethod
    def parse_response(response_txt: str) -> dict:
        info, pub, uid = None, None, None
        response_txt = [i.rstrip() for i in response_txt.split('\n')]
        for r in response_txt:
            if 'info' in r:
                info = r.split('info:')[-1]
            if 'pub' in r:
                pub = r.split('pub:')[-1]
            if 'uid' in r:
                uid = r.split('uid:')[-1]

        if pub is None and uid is None:
            return {}

        return {
            'info': info,
            'pub': pub,
            'uid': uid,
            'email': re.search(r'<(.*?)>', uid).group(1)
        }

    @staticmethod
    def get_response(user):
        feed_url = f'{Protonmail._feed}{user}'
        res_txt = requests.get(feed_url).text
        return Protonmail.parse_response(res_txt)

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


# if __name__ == "__main__":
#     res = Protonmail.get('admin')
#     print(res)
#     res = Protonmail.get('admin@protonmail.com')
#     print(res)
