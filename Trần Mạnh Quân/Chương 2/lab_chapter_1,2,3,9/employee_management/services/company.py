from models.employee import Employee
from exceptions.employee_exceptions import EmployeeNotFoundError, DuplicateEmployeeError

class Company:
    def __init__(self, name="Công ty ABC"):
        self.name = name
        self.employees = {} # emp_id -> Employee object

    def add_employee(self, employee):
        if employee.emp_id in self.employees:
            raise DuplicateEmployeeError(employee.emp_id)
        self.employees[employee.emp_id] = employee

    def remove_employee(self, emp_id):
        if emp_id not in self.employees:
            raise EmployeeNotFoundError(emp_id)
        del self.employees[emp_id]

    def find_employee_by_id(self, emp_id):
        if emp_id not in self.employees:
            raise EmployeeNotFoundError(emp_id)
        return self.employees[emp_id]

    def find_employees_by_name(self, name):
        results = [e for e in self.employees.values() if name.lower() in e.name.lower()]
        if not results:
            raise EmployeeNotFoundError(name)
        return results

    def get_all_employees(self):
        return list(self.employees.values())

    def get_employees_by_type(self, emp_type):
        return [e for e in self.employees.values() if e.__class__.__name__.lower() == emp_type.lower()]

    def get_top_performers(self):
        return sorted(self.employees.values(), key=lambda x: x.performance_score, reverse=True)

    def calculate_total_payroll(self):
        return sum(e.calculate_salary() for e in self.employees.values())

    def get_top_3_salaries(self):
        return sorted(self.employees.values(), key=lambda x: x.calculate_salary(), reverse=True)[:3]
