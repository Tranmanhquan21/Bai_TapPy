from .employee import Employee

class Intern(Employee):
    def __init__(self, emp_id, name, age, base_salary, major):
        super().__init__(emp_id, name, age, base_salary)
        self._major = major

    @property
    def major(self): return self._major

    def calculate_salary(self):
        # Lương = Lương cơ bản * 0.8 + Thưởng hiệu suất
        return (self.base_salary * 0.8) + (self.performance_score / 10) * 1000000

    def __str__(self):
        return f"[Intern] " + super().__str__() + f" | Chuyên ngành: {self._major}"
