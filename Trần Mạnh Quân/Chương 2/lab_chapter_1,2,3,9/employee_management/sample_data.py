"""Dữ liệu mẫu để demo hệ thống (không ghi file, chỉ nạp vào Company khi chạy)."""

from models import Manager, Developer, Intern


def seed_sample_employees(company):
    """
    Thêm một bộ nhân viên mẫu nếu danh sách đang trống.
    Trả về True nếu đã nạp, False nếu đã có dữ liệu (bỏ qua).
    """
    if company.employees:
        return False

    samples = [
        Manager("M001", "Nguyễn Văn An", 42, 25_000_000, 8, tenure_months=120),
        Manager("M002", "Trần Thị Bình", 38, 22_000_000, 5, tenure_months=84),
        Developer("D101", "Lê Hoàng Nam", 29, 18_000_000, "Python", tenure_months=48),
        Developer("D102", "Phạm Minh Tuấn", 31, 17_000_000, "Java", tenure_months=60),
        Developer("D103", "Đỗ Thu Hà", 27, 16_000_000, "JavaScript", tenure_months=36),
        Intern("I201", "Vũ Quốc Huy", 22, 8_000_000, "Công nghệ thông tin", tenure_months=6),
        Intern("I202", "Hoàng Ngọc Lan", 21, 7_500_000, "Khoa học máy tính", tenure_months=5),
    ]

    for emp in samples:
        company.add_employee(emp)

    # Điểm hiệu suất & dự án (sau khi đã add vào company)
    company.find_employee_by_id("M001").performance_score = 8.5
    company.find_employee_by_id("M002").performance_score = 7.0
    company.find_employee_by_id("D101").performance_score = 9.0
    company.find_employee_by_id("D102").performance_score = 7.5
    company.find_employee_by_id("D103").performance_score = 6.5
    company.find_employee_by_id("I201").performance_score = 5.5
    company.find_employee_by_id("I202").performance_score = 8.0

    e = company.find_employee_by_id("M001")
    e.add_project("ERP nội bộ")
    e.add_project("Mobile CRM")

    e = company.find_employee_by_id("D101")
    e.add_project("API thanh toán")
    e.add_project("Tích hợp webhook")

    e = company.find_employee_by_id("D102")
    e.add_project("Hệ thống kho")

    return True
