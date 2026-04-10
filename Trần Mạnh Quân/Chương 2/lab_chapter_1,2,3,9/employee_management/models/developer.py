from .employee import Employee

class Developer(Employee):
    def __init__(self, emp_id, name, age, base_salary, programming_language):
        super().__init__(emp_id, name, age, base_salary)
        self._programming_language = programming_language

    @property
    def programming_language(self): return self._programming_language

    def calculate_salary(self):
        # Lương = Lương cơ bản + Phụ cấp ngôn ngữ (2M) + Thưởng hiệu suất
        language_bonus = 2000000
        performance_bonus = (self.performance_score / 10) * self.base_salary * 0.3
        return self.base_salary + language_bonus + performance_bonus

    def __str__(self):
        return f"[Developer] " + super().__str__() + f" | Ngôn ngữ: {self._programming_language}"
