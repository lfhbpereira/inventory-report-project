from collections import Counter
from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(list):
        oldest_manufacturing_date = min(
            item["data_de_fabricacao"]
            for item in list
        )

        nearest_expiration_date = min(
            item["data_de_validade"]
            for item in list
            if item["data_de_validade"] > str(datetime.today())
        )

        companies = [item["nome_da_empresa"] for item in list]
        company_with_most_products = Counter(companies).most_common()[0]

        return (
            f"Data de fabricação mais antiga: {oldest_manufacturing_date}\n"
            f"Data de validade mais próxima: {nearest_expiration_date}\n"
            f"Empresa com mais produtos: {company_with_most_products[0]}"
        )
