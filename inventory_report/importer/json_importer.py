from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        if path.endswith(".json"):
            with open(path) as file:
                data = json.load(file)

                return data

        raise ValueError("Arquivo inválido")
