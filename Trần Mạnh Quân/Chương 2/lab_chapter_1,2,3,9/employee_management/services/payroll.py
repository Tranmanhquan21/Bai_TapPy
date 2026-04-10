class Payroll:
    @staticmethod
    def generate_salary_report(employees):
        report = []
        for emp in employees:
            salary = emp.calculate_salary()
            report.append({
                "id": emp.emp_id,
                "name": emp.name,
                "type": emp.__class__.__name__,
                "salary": salary
            })
        return report

    @staticmethod
    def calculate_average_projects(employees):
        if not employees: return 0
        total_projects = sum(len(e.projects) for e in employees)
        return total_projects / len(employees)
