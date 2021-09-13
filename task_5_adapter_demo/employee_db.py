from task_5_adapter_demo.employee import Employee


class EmployeeDB(Employee):

    def __init__(self, id, firstname, lastname, email):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

    def get_id(self):
        return self.id

    def get_firstname(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname

    def get_email(self):
        return self.email

