"""
Công thức đền bù (demo nội bộ — có thể chỉnh hệ số).

- Đền bù chấm dứt HĐLĐ: dựa trên lương CB, thâm niên (tháng), điểm hiệu suất, chức danh.
- Đền bù gắn với một dự án: phần thưởng đóng góp khi tính toán hoàn thành / milestone.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.employee import Employee


class Compensation:
    """Hệ số chức danh áp dụng cho các khoản đền bù."""

    ROLE_FACTOR = {
        "Manager": 1.15,
        "Developer": 1.0,
        "Intern": 0.55,
    }

    @classmethod
    def _role(cls, emp: "Employee") -> float:
        return cls.ROLE_FACTOR.get(emp.__class__.__name__, 1.0)

    @staticmethod
    def calculate_contract_severance(emp: "Employee") -> float:
        """
        Đền bù khi nghỉ việc / chấm dứt hợp đồng (quy ước sáng tạo):

        - Quy đổi thâm niên: số 'tháng lương đền bù' = min(6, max(1, tenure_months / 12)),
          tức từ 1 đến 6 tháng lương cơ bản tùy thâm niên (mỗi 12 thám làm thêm ~1 tháng đền bù, trần 6).
        - Hệ số hiệu suất: 0.5 + (điểm HS / 10) × 0.5  → khoảng 0.5–1.0.
        - Nhân hệ số chức danh (Manager cao hơn Intern).

        Kết quả được chặn trong [0.5 × lương CB, 6 × lương CB] để tránh số quá lệch demo.
        """
        tenure = getattr(emp, "tenure_months", 12)
        months_equiv = min(6.0, max(1.0, tenure / 12.0))
        perf_factor = 0.5 + (emp.performance_score / 10.0) * 0.5
        role = Compensation._role(emp)
        raw = emp.base_salary * months_equiv * perf_factor * role
        lo = emp.base_salary * 0.5
        hi = emp.base_salary * 6.0
        return max(lo, min(raw, hi))

    @staticmethod
    def calculate_project_compensation(emp: "Employee", project_name: str) -> float:
        """
        Đền bù / thưởng milestone gắn với một dự án (quy ước sáng tạo):

        - Chỉ áp dụng nếu nhân viên đang có tên dự án trong danh sách.
        - Lấy phần lương thực tế 'quy cho mỗi dự án' = lương thực tế / số dự án đang tham gia.
        - Thưởng = 22% phần đó × (điểm HS / 10) × hệ số chức danh × (1 + thâm niên năm / 20),
          nghĩa là người nhiều kinh nghiệm và hiệu suất cao được đền bù dự án lớn hơn.

        Làm tròn đến hàng nghìn đồng.
        """
        if project_name.strip() not in emp.projects:
            raise ValueError("Nhân viên không tham gia dự án này (kiểm tra tên chính xác).")

        n = max(len(emp.projects), 1)
        share = emp.calculate_salary() / n
        perf = emp.performance_score / 10.0
        role = Compensation._role(emp)
        tenure_years = getattr(emp, "tenure_months", 12) / 12.0
        seniority = 1.0 + min(tenure_years / 20.0, 0.5)

        bonus = share * 0.22 * perf * role * seniority
        return round(bonus / 1000.0) * 1000.0
