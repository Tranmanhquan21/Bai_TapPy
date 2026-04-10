from .employee import Employee

class Manager(Employee):
    def __init__(self, emp_id, name, age, base_salary, team_size):
        super().__init__(emp_id, name, age, base_salary)
        self._team_size = team_size

    @property
    def team_size(self): return self._team_size

    def calculate_salary(self):
        # Lương = Lương cơ bản + Phụ cấp quản lý (5M/nhân viên) + Thưởng hiệu suất
        allowance = self._team_size * 5000000
        performance_bonus = (self.performance_score / 10) * self.base_salary * 0.5
        return self.base_salary + allowance + performance_bonus

    def __str__(self):
        return f"[Manager] " + super().__str__() + f" | Team: {self._team_size}"
