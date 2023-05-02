from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


def test_decorar_relatorio():
    product = [
        {
            "id": "1",
            "nome_do_produto": "Nicotine Polacrilex",
            "nome_da_empresa": "Target Corporation",
            "data_de_fabricacao": "2021-02-18",
            "data_de_validade": "2023-09-17",
            "numero_de_serie": "CR25 1551 4467 2549 4402 1",
            "instrucoes_de_armazenamento": "instrucao 1"
        }
    ]

    colored_simple_report = ColoredReport(SimpleReport).generate(product)

    colored_complete_report = ColoredReport(CompleteReport).generate(product)

    assert ("\033[36m" in colored_simple_report) is True
    assert ("\033[36m" in colored_complete_report) is True
