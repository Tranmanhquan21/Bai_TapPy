from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, emp_id, name, age, base_salary):
        self._emp_id = emp_id
        self._name = name
        self._age = age
        self._base_salary = base_salary
        self._performance_score = 0.0
        self._projects = []

    @property
    def emp_id(self): return self._emp_id
    
    @property
    def name(self): return self._name
    
    @property
    def age(self): return self._age
    
    @property
    def base_salary(self): return self._base_salary
    
    @base_salary.setter
    def base_salary(self, value):
        self._base_salary = value

    @property
    def performance_score(self): return self._performance_score
    
    @performance_score.setter
    def performance_score(self, value):
        if 0 <= value <= 10:
            self._performance_score = value
        else:
            raise ValueError("Điểm hiệu suất phải từ 0 đến 10")

    @property
    def projects(self): return self._projects

    @abstractmethod
    def calculate_salary(self):
        """Abstract method to be implemented by subclasses."""
        pass

    def add_project(self, project_name):
        if len(self._projects) >= 5:
            from exceptions.employee_exceptions import ProjectAllocationError
            raise ProjectAllocationError()
        if project_name not in self._projects:
            self._projects.append(project_name)

    def remove_project(self, project_name):
        if project_name in self._projects:
            self._projects.remove(project_name)

    def __str__(self):
        return f"ID: {self._emp_id} | Tên: {self._name} | Tuổi: {self._age} | Lương CB: {self._base_salary:,.0f} | Điểm HS: {self._performance_score}"
