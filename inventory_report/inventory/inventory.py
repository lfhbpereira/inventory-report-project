from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport

reports = {"simples": SimpleReport, "completo": CompleteReport}


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        if path.endswith(".csv"):
            data = CsvImporter.import_data(path)
        elif path.endswith(".json"):
            data = JsonImporter.import_data(path)
        elif path.endswith(".xml"):
            data = XmlImporter.import_data(path)

        return reports[type].generate(data)
