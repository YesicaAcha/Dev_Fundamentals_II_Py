from task_6_design_patterns.problem_1_invoices.invoice.invoice import Invoice


class BolivianInvoice(Invoice):

    def __init__(self, nit, name):
        self.nit = nit
        self.name = name

    def get_details(self):
        return "NIT: {0}, Name: {1}".format(self.nit, self.name)
