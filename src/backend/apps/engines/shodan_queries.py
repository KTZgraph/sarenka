import json
import os
from pathlib import Path


class ShodanQueries:
    __http_component_source = 'feeds\\shodan\\http_component.json'

    def __init__(self) -> None:
        self.dir_path = Path(__file__).parent.absolute()

    def get_http_component(self):
        file_path = os.path.join(
            self.dir_path, ShodanQueries.__http_component_source)

        with open(file_path) as json_file:
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
