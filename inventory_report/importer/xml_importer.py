from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if path.endswith(".xml"):
            with open(path) as file:
                data = xmltodict.parse(file.read())["dataset"]["record"]

                return list(data)

        raise ValueError("Arquivo inválido")
