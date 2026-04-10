class EmployeeError(Exception):
    """Base class for exceptions in this module."""
    pass

class InvalidAgeError(EmployeeError):
    """Exception raised for invalid employee age."""
    def __init__(self, age, message="Tuổi phải trong khoảng từ 18 đến 65"):
        self.age = age
        self.message = f"{message} (Nhập vào: {age})"
        super().__init__(self.message)

class InvalidSalaryError(EmployeeError):
    """Exception raised for invalid employee salary."""
    def __init__(self, salary, message="Lương phải là số dương lớn hơn 0"):
        self.salary = salary
        self.message = f"{message} (Nhập vào: {salary})"
        super().__init__(self.message)

class EmployeeNotFoundError(EmployeeError):
    """Exception raised when an employee is not found."""
    def __init__(self, identifier, message="Không tìm thấy nhân viên"):
        self.identifier = identifier
        self.message = f"{message} với mã/tên: {identifier}"
        super().__init__(self.message)

class ProjectAllocationError(EmployeeError):
    """Exception raised when project allocation fails."""
    def __init__(self, message="Nhân viên đã đạt tối đa 5 dự án"):
        self.message = message
        super().__init__(self.message)

class DuplicateEmployeeError(EmployeeError):
    """Exception raised when an employee ID already exists."""
    def __init__(self, emp_id, message="Mã nhân viên đã tồn tại"):
        self.emp_id = emp_id
        self.message = f"{message}: {emp_id}"
        super().__init__(self.message)
