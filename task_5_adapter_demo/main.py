from task_5_adapter_demo.employee_adapter_ldap import EmployeeAdapterLdap
from task_5_adapter_demo.employee_db import EmployeeDB
from task_5_adapter_demo.employee_ldap import EmployeeLdap

if __name__ == '__main__':
    employees = []

    employee_db = EmployeeDB("1234", "Charlie", "Brown", "charlie@brown.com")
    employees.append(employee_db)

    employee_ldap = EmployeeLdap("exampleCN", "Snow", "Jon", "jon@snow.com")
    employees.append(EmployeeAdapterLdap(employee_ldap))

    for employee in employees:
        print("Id: {0}, firstname: {1}, lastname: {2}, email: {3}"
              .format(employee.get_id(), employee.get_firstname(), employee.get_lastname(), employee.get_email()))
