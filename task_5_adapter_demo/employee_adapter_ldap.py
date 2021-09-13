from task_5_adapter_demo.employee import Employee


class EmployeeAdapterLdap(Employee):

    __employeeLdap = None

    def __init__(self, employee_ldap):
        self.__employeeLdap = employee_ldap

    def get_id(self):
        return self.__employeeLdap.cn

    def get_firstname(self):
        return self.__employeeLdap.given_name

    def get_lastname(self):
        return self.__employeeLdap.surname

    def get_email(self):
        return self.__employeeLdap.mail
