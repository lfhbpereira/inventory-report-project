from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        if path.endswith(".csv"):
            with open(path) as file:
                data = csv.DictReader(file)

                return list(data)

        raise ValueError("Arquivo inválido")
