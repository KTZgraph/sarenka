import json


class ShodanQueries:
    __http_component_source = 'http_component.json'

    def __init__(self) -> None:
        pass

    def get_http_component(self):
        with open('http_component.json') as json_file:
            data = json.loads(json_file.read())
        return data


shodan_queries = [
    {
        "id_": "1",
        "name": "nginx",
        "product_url": "https://www.nginx.com/",
        "description": "WWW server",
        "category": "",
        "type": "product",
        "url": "https://www.shodan.io/search?query=product%3A%22nginx%22",
        "query": 'product:"nginx"',
        "notes": "",
        "cves": ["CVE-1", "CVE-2"]
    },
    {},
    {},
    {},
]
