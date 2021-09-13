class EmployeeLdap:

    def __init__(self, cn, surname, given_name, mail):
        self.cn = cn
        self.surname = surname
        self.given_name = given_name
        self.mail = mail

    def get_cn(self):
        return self.cn

    def get_surname(self):
        return self.surname

    def get_give_name(self):
        return self.given_name

    def get_mail(self):
        return self.mail
