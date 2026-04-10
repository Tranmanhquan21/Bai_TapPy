import re
from exceptions.employee_exceptions import InvalidAgeError, InvalidSalaryError

class Validators:
    @staticmethod
    def validate_age(age):
        if not (18 <= age <= 65):
            raise InvalidAgeError(age)
        return True

    @staticmethod
    def validate_salary(salary):
        if salary <= 0:
            raise InvalidSalaryError(salary)
        return True

    @staticmethod
    def validate_email(email):
        # Biểu thức chính quy cho email đơn giản
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            raise ValueError("Email sai định dạng (thiếu @ hoặc tên miền)")
        return True
