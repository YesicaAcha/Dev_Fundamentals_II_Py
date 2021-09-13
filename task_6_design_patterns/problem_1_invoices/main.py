from task_6_design_patterns.problem_1_invoices.invoice_factory import InvoiceFactory


if __name__ == '__main__':
    invoice_factory = InvoiceFactory()
    country = input("Enter the name of the country you are purchasing from: ")

    invoice = invoice_factory.create_invoice(country)

    print(f"The details of your invoice are: {invoice.get_details()}")
