from task_6_design_patterns.problem_1_invoices.invoice.invoice import Invoice


class MexicanInvoice(Invoice):

    def __init__(self, rfc, receptor, cfdi):
        self.rfc = rfc
        self.receptor = receptor
        self.cfdi = cfdi

    def get_details(self):
        return "RFC: {0}, Receptor: {1}, CFDI: {2}".format(self.rfc, self.receptor, self.cfdi)
