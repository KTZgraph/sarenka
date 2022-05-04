import os

import pandas
import json
from pathlib import Path


class CWETOP25:
    __source_filepath = "..\\feeds\\cwes\\1350.csv"
    __source_url = "https://cwe.mitre.org/data/csv/1350.csv.zip"
    __output_filepath = "cwe_top_25.json"

    @property
    def output_path(self):
        return CWETOP25.get_output_path()

    @staticmethod
    def get_output_path():
        dir_path = Path(__file__).parent.absolute()
        return os.path.join(dir_path, CWETOP25.__output_filepath)

    @staticmethod
    def download():
        raise NotImplementedError("Pobieranie pliku nie zaimplementowane")

    def parse(self):
        if not Path(self.output_path).is_file():
            CWETOP25.download()

        df = pandas.read_csv(
            CWETOP25.__source_filepath,
            skiprows=0,
            names=(
                "cwe_id",
                "name",
                "weakness_abstraction",
                "status",
                "description",
                "extended_description",
                "related_weaknesses",
                "weakness_ordinalities",
                "applicable_platforms",
                "background_details",
                "alternate_terms",
                "modes_of_introduction",
                "exploitation_factors",
                "likelihood_of_exploit",
                "common_consequences",
                "detection_methods",
                "potential_mitigations",
                "observed_examples",
                "functional_areas",
                "affected_resources",
                "taxonomy_mappings",
                "related_attack_patterns",
                "notes",
            ),
        )

        df.to_json(self.output_path, orient="records")

    def get(self):
        if not Path(self.output_path).is_file():
            CWETOP25.parse()

        with open(self.output_path) as json_file:
            data = json.loads(json_file.read())
        return data[1:]
