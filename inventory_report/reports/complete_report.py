from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport:
    @staticmethod
    def generate(list):
        simple_report = SimpleReport.generate(list)

        companies = [item["nome_da_empresa"] for item in list]
        companies_products = Counter(companies).items()

        companies_total = ""
        for company, quantity in companies_products:
            companies_total += f"- {company}: {quantity}\n"

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{companies_total}"
        )
