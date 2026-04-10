import os
import sys

# Thêm thư mục hiện tại vào sys.path để import các module local
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models import Manager, Developer, Intern
from services.company import Company
from services.payroll import Payroll
from utils.validators import Validators
from utils.formatters import Formatters
from exceptions.employee_exceptions import EmployeeError

class EmployeeManagementApp:
    def __init__(self):
        self.company = Company()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def input_employee_data(self):
        while True:
            try:
                emp_id = input("Nhập ID: ")
                name = input("Nhập tên: ")
                age = int(input("Nhập tuổi: "))
                Validators.validate_age(age)
                base_salary = float(input("Nhập lương cơ bản: "))
                Validators.validate_salary(base_salary)
                return emp_id, name, age, base_salary
            except ValueError as e:
                print(f"Lỗi: {e}. Vui lòng nhập lại số.")
            except EmployeeError as e:
                print(f"Lỗi: {e}. Vui lòng nhập lại.")

    def run(self):
        while True:
            print(Formatters.format_header("HỆ THỐNG QUẢN LÝ NHÂN VIÊN CÔNG TY ABC"))
            print("1. Thêm nhân viên mới")
            print("   a. Thêm Manager | b. Thêm Developer | c. Thêm Intern")
            print("2. Hiển thị danh sách nhân viên")
            print("   a. Tất cả | b. Theo loại | c. Theo hiệu suất")
            print("3. Tìm kiếm nhân viên")
            print("   a. Theo ID | b. Theo tên")
            print("4. Quản lý lương")
            print("   a. Tính lương cá nhân | b. Tổng lương công ty | c. Top 3")
            print("5. Quản lý dự án")
            print("   a. Phân công | b. Xóa khỏi dự án | c. Hiển thị dự án")
            print("6. Đánh giá hiệu suất")
            print("7. Quản lý nhân sự (Xóa, Tăng lương, Thăng chức)")
            print("8. Thống kê báo cáo")
            print("9. Thoát")
            
            choice = input("\nChọn chức năng (1-9): ").lower()

            try:
                if choice == '1a':
                    id, name, age, salary = self.input_employee_data()
                    tsize = int(input("Nhập quy mô team: "))
                    self.company.add_employee(Manager(id, name, age, salary, tsize))
                    print("Đã thêm Manager thành công!")
                
                elif choice == '1b':
                    id, name, age, salary = self.input_employee_data()
                    lang = input("Nhập ngôn ngữ lập trình: ")
                    self.company.add_employee(Developer(id, name, age, salary, lang))
                    print("Đã thêm Developer thành công!")
                
                elif choice == '1c':
                    id, name, age, salary = self.input_employee_data()
                    major = input("Nhập chuyên ngành: ")
                    self.company.add_employee(Intern(id, name, age, salary, major))
                    print("Đã thêm Intern thành công!")

                elif choice == '2a':
                    for emp in self.company.get_all_employees():
                        print(emp)
                
                elif choice == '3a':
                    eid = input("Nhập ID cần tìm: ")
                    print(self.company.find_employee_by_id(eid))

                elif choice == '4b':
                    total = self.company.calculate_total_payroll()
                    print(f"Tổng lương công ty: {Formatters.format_currency(total)}")

                elif choice == '6':
                    eid = input("Nhập ID nhân viên: ")
                    emp = self.company.find_employee_by_id(eid)
                    score = float(input("Nhập điểm hiệu suất (0-10): "))
                    emp.performance_score = score
                    print("Đã cập nhật điểm hiệu suất!")

                elif choice == '9':
                    print("Cảm ơn bạn đã sử dụng hệ thống!")
                    break
                
                else:
                    print("Chức năng đang được cập nhật hoặc nhập sai.")

            except Exception as e:
                print(f"CÓ LỖI XẢY RA: {e}")
            
            input("\nNhấn Enter để tiếp tục...")
            self.clear_screen()

if __name__ == "__main__":
    app = EmployeeManagementApp()
    app.run()
