from task_6_design_patterns.problem_1_invoices.invoice.bolivian_invoice import BolivianInvoice
from task_6_design_patterns.problem_1_invoices.invoice.mexican_invoice import MexicanInvoice


class InvoiceFactory:
    def create_invoice(self, country):

        if country == 'Bolivia':
            nit = input("Enter your NIT o CI: ")
            name = input("Enter your name: ")
            return BolivianInvoice(nit, name)

        elif country == 'Mexico':
            rfc = input("Enter your RFC: ")
            receptor = input("Enter the receptor: ")
            cfdi = input("Enter your CFDI: ")
            return MexicanInvoice(rfc, receptor, cfdi)




