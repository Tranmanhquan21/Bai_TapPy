"""
Giao diện đồ họa (Tkinter) cho hệ thống quản lý nhân viên.
Chạy: python main.py  (từ thư mục employee_management)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

from models import Manager, Developer, Intern
from services.company import Company
from services.payroll import Payroll
from services.compensation import Compensation
from utils.validators import Validators
from utils.formatters import Formatters
from exceptions.employee_exceptions import EmployeeError
from sample_data import seed_sample_employees


class EmployeeManagementGUI:
    def __init__(self):
        self.company = Company()
        seed_sample_employees(self.company)
        self.root = tk.Tk()
        self.root.title("Quản lý nhân viên — Công ty ABC")
        self.root.minsize(880, 560)
        self.root.geometry("960x620")

        style = ttk.Style()
        if "vista" in style.theme_names():
            style.theme_use("vista")
        style.configure("TNotebook.Tab", padding=[12, 6])

        self._build_ui()

    def _build_ui(self):
        main = ttk.Frame(self.root, padding=10)
        main.pack(fill=tk.BOTH, expand=True)

        hdr = ttk.Label(
            main,
            text="HỆ THỐNG QUẢN LÝ NHÂN VIÊN CÔNG TY ABC",
            font=("Segoe UI", 14, "bold"),
        )
        hdr.pack(anchor=tk.W, pady=(0, 8))

        nb = ttk.Notebook(main)
        nb.pack(fill=tk.BOTH, expand=True)

        self._tab_add(nb)
        self._tab_list(nb)
        self._tab_search(nb)
        self._tab_payroll(nb)
        self._tab_project_management(nb)
        self._tab_performance_projects(nb)
        self._tab_hr(nb)
        self._tab_remove(nb)

    def _tab_add(self, nb):
        tab = ttk.Frame(nb, padding=12)
        nb.add(tab, text="Thêm nhân viên")

        f = ttk.LabelFrame(tab, text="Thông tin chung", padding=10)
        f.pack(fill=tk.X, pady=(0, 8))

        self.var_emp_id = tk.StringVar()
        self.var_name = tk.StringVar()
        self.var_age = tk.StringVar()
        self.var_salary = tk.StringVar()
        self.var_tenure = tk.StringVar(value="12")
        self.var_emp_type = tk.StringVar(value="Manager")

        row = 0
        for label, var in [
            ("Mã ID:", self.var_emp_id),
            ("Họ tên:", self.var_name),
            ("Tuổi:", self.var_age),
            ("Lương cơ bản (VNĐ):", self.var_salary),
            ("Thâm niên (tháng):", self.var_tenure),
        ]:
            ttk.Label(f, text=label).grid(row=row, column=0, sticky=tk.W, padx=(0, 8), pady=4)
            ttk.Entry(f, textvariable=var, width=40).grid(row=row, column=1, sticky=tk.W, pady=4)
            row += 1

        ttk.Label(f, text="Loại nhân viên:").grid(row=row, column=0, sticky=tk.W, pady=4)
        cb = ttk.Combobox(
            f,
            textvariable=self.var_emp_type,
            values=("Manager", "Developer", "Intern"),
            state="readonly",
            width=37,
        )
        cb.grid(row=row, column=1, sticky=tk.W, pady=4)
        cb.bind("<<ComboboxSelected>>", lambda e: self._toggle_extra_fields())
        row += 1

        self.frame_extra = ttk.LabelFrame(tab, text="Thông tin riêng theo loại", padding=10)
        self.frame_extra.pack(fill=tk.X, pady=(0, 8))

        self.var_team = tk.StringVar()
        self.var_lang = tk.StringVar()
        self.var_major = tk.StringVar()

        self.lbl_team = ttk.Label(self.frame_extra, text="Quy mô team:")
        self.ent_team = ttk.Entry(self.frame_extra, textvariable=self.var_team, width=40)
        self.lbl_lang = ttk.Label(self.frame_extra, text="Ngôn ngữ lập trình:")
        self.ent_lang = ttk.Entry(self.frame_extra, textvariable=self.var_lang, width=40)
        self.lbl_major = ttk.Label(self.frame_extra, text="Chuyên ngành:")
        self.ent_major = ttk.Entry(self.frame_extra, textvariable=self.var_major, width=40)

        self._toggle_extra_fields()

        ttk.Button(tab, text="Thêm nhân viên", command=self._on_add_employee).pack(anchor=tk.W)

    def _toggle_extra_fields(self):
        for w in self.frame_extra.winfo_children():
            w.grid_forget()

        t = self.var_emp_type.get()
        if t == "Manager":
            self.lbl_team.grid(row=0, column=0, sticky=tk.W, padx=(0, 8), pady=4)
            self.ent_team.grid(row=0, column=1, sticky=tk.W, pady=4)
        elif t == "Developer":
            self.lbl_lang.grid(row=0, column=0, sticky=tk.W, padx=(0, 8), pady=4)
            self.ent_lang.grid(row=0, column=1, sticky=tk.W, pady=4)
        else:
            self.lbl_major.grid(row=0, column=0, sticky=tk.W, padx=(0, 8), pady=4)
            self.ent_major.grid(row=0, column=1, sticky=tk.W, pady=4)

    def _parse_common(self):
        emp_id = self.var_emp_id.get().strip()
        name = self.var_name.get().strip()
        age = int(self.var_age.get().strip())
        base_salary = float(self.var_salary.get().strip().replace(",", ""))
        tenure = int(self.var_tenure.get().strip())
        if tenure < 1:
            raise ValueError("Thâm niên phải từ 1 tháng trở lên.")
        Validators.validate_age(age)
        Validators.validate_salary(base_salary)
        return emp_id, name, age, base_salary, tenure

    def _on_add_employee(self):
        try:
            emp_id, name, age, base_salary, tenure = self._parse_common()
            t = self.var_emp_type.get()
            if t == "Manager":
                ts = int(self.var_team.get().strip())
                self.company.add_employee(Manager(emp_id, name, age, base_salary, ts, tenure_months=tenure))
            elif t == "Developer":
                lang = self.var_lang.get().strip()
                self.company.add_employee(Developer(emp_id, name, age, base_salary, lang, tenure_months=tenure))
            else:
                major = self.var_major.get().strip()
                self.company.add_employee(Intern(emp_id, name, age, base_salary, major, tenure_months=tenure))
            messagebox.showinfo("Thành công", f"Đã thêm {t} thành công.")
            self._refresh_all()
        except ValueError as e:
            messagebox.showerror("Lỗi nhập liệu", str(e))
        except EmployeeError as e:
            messagebox.showerror("Lỗi", str(e))

    def _tab_list(self, nb):
        tab = ttk.Frame(nb, padding=12)
        nb.add(tab, text="Danh sách")

        bar = ttk.Frame(tab)
        bar.pack(fill=tk.X, pady=(0, 8))

        ttk.Label(bar, text="Lọc:").pack(side=tk.LEFT, padx=(0, 6))
        self.var_filter = tk.StringVar(value="all")
        for val, text in [
            ("all", "Tất cả"),
            ("manager", "Manager"),
            ("developer", "Developer"),
            ("intern", "Intern"),
            ("perf", "Theo hiệu suất (cao → thấp)"),
        ]:
            ttk.Radiobutton(bar, text=text, variable=self.var_filter, value=val, command=self._refresh_all).pack(
                side=tk.LEFT, padx=4
            )
        ttk.Button(bar, text="Làm mới", command=self._refresh_all).pack(side=tk.RIGHT)

        cols = ("id", "name", "kind", "age", "base", "score", "salary", "extra")
        self.tree = ttk.Treeview(tab, columns=cols, show="headings", height=16)
        headings = {
            "id": "Mã ID",
            "name": "Họ tên",
            "kind": "Loại",
            "age": "Tuổi",
            "base": "Lương CB",
            "score": "Điểm HS",
            "salary": "Lương thực tế",
            "extra": "Ghi chú",
        }
        widths = {"id": 90, "name": 140, "kind": 90, "age": 50, "base": 110, "score": 70, "salary": 120, "extra": 180}
        for c in cols:
            self.tree.heading(c, text=headings[c])
            self.tree.column(c, width=widths[c], anchor=tk.W)

        scroll = ttk.Scrollbar(tab, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scroll.set)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)

    def _employees_for_display(self):
        f = self.var_filter.get()
        if f == "all":
            emps = self.company.get_all_employees()
        elif f == "perf":
            emps = self.company.get_top_performers()
        else:
            emps = self.company.get_employees_by_type(f.capitalize())
        return emps

    def _extra_note(self, emp):
        cn = emp.__class__.__name__
        if cn == "Manager":
            return f"Team: {emp.team_size}"
        if cn == "Developer":
            return f"NNLT: {emp.programming_language}"
        return f"Ngành: {emp.major}"

    def _refresh_tree(self):
        if not hasattr(self, "tree"):
            return
        for i in self.tree.get_children():
            self.tree.delete(i)
        try:
            emps = self._employees_for_display()
        except Exception:
            emps = []
        for emp in emps:
            self.tree.insert(
                "",
                tk.END,
                values=(
                    emp.emp_id,
                    emp.name,
                    emp.__class__.__name__,
                    emp.age,
                    Formatters.format_currency(emp.base_salary),
                    f"{emp.performance_score:.1f}",
                    Formatters.format_currency(emp.calculate_salary()),
                    self._extra_note(emp),
                ),
            )

    def _tab_search(self, nb):
        tab = ttk.Frame(nb, padding=12)
        nb.add(tab, text="Tìm kiếm")

        f = ttk.Frame(tab)
        f.pack(fill=tk.X, pady=(0, 8))
        self.var_search_id = tk.StringVar()
        self.var_search_name = tk.StringVar()
        ttk.Label(f, text="Theo mã ID:").grid(row=0, column=0, sticky=tk.W, padx=(0, 8))
        ttk.Entry(f, textvariable=self.var_search_id, width=30).grid(row=0, column=1, sticky=tk.W)
        ttk.Button(f, text="Tìm", command=self._search_id).grid(row=0, column=2, padx=8)

        ttk.Label(f, text="Theo tên (một phần):").grid(row=1, column=0, sticky=tk.W, pady=(8, 0))
        ttk.Entry(f, textvariable=self.var_search_name, width=30).grid(row=1, column=1, sticky=tk.W, pady=(8, 0))
        ttk.Button(f, text="Tìm", command=self._search_name).grid(row=1, column=2, padx=8, pady=(8, 0))

        self.txt_search = scrolledtext.ScrolledText(tab, height=18, wrap=tk.WORD, font=("Consolas", 10))
        self.txt_search.pack(fill=tk.BOTH, expand=True)

    def _search_id(self):
        self.txt_search.delete("1.0", tk.END)
        try:
            eid = self.var_search_id.get().strip()
            emp = self.company.find_employee_by_id(eid)
            self.txt_search.insert(tk.END, str(emp) + "\n")
            self.txt_search.insert(tk.END, f"Lương thực tế: {Formatters.format_currency(emp.calculate_salary())}\n")
        except EmployeeError as err:
            messagebox.showwarning("Không tìm thấy", str(err))

    def _search_name(self):
        self.txt_search.delete("1.0", tk.END)
        try:
            name = self.var_search_name.get().strip()
            for emp in self.company.find_employees_by_name(name):
                self.txt_search.insert(tk.END, str(emp) + "\n")
                self.txt_search.insert(
                    tk.END, f"  Lương thực tế: {Formatters.format_currency(emp.calculate_salary())}\n\n"
                )
        except EmployeeError as err:
            messagebox.showwarning("Không tìm thấy", str(err))

    def _tab_payroll(self, nb):
        tab = ttk.Frame(nb, padding=12)
        nb.add(tab, text="Lương & thống kê")

        btnf = ttk.Frame(tab)
        btnf.pack(fill=tk.X, pady=(0, 8))
        ttk.Button(btnf, text="Tổng quỹ lương", command=self._show_total).pack(side=tk.LEFT, padx=(0, 8))
        ttk.Button(btnf, text="Top 3 lương cao", command=self._show_top3).pack(side=tk.LEFT, padx=(0, 8))
        ttk.Button(btnf, text="Báo cáo chi tiết", command=self._show_report).pack(side=tk.LEFT)

        self.txt_pay = scrolledtext.ScrolledText(tab, height=22, wrap=tk.WORD, font=("Consolas", 10))
        self.txt_pay.pack(fill=tk.BOTH, expand=True)

    def _show_total(self):
        total = self.company.calculate_total_payroll()
        self.txt_pay.delete("1.0", tk.END)
        self.txt_pay.insert(tk.END, f"Tổng quỹ lương công ty: {Formatters.format_currency(total)}\n")

    def _show_top3(self):
        self.txt_pay.delete("1.0", tk.END)
        top = self.company.get_top_3_salaries()
        if not top:
            self.txt_pay.insert(tk.END, "Chưa có nhân viên nào.\n")
            return
        self.txt_pay.insert(tk.END, "Top 3 lương cao nhất:\n\n")
        for i, emp in enumerate(top, 1):
            self.txt_pay.insert(
                tk.END, f"{i}. {emp.name} ({emp.emp_id}) — {Formatters.format_currency(emp.calculate_salary())}\n"
            )

    def _show_report(self):
        emps = self.company.get_all_employees()
        self.txt_pay.delete("1.0", tk.END)
        if not emps:
            self.txt_pay.insert(tk.END, "Chưa có nhân viên.\n")
            return
        report = Payroll.generate_salary_report(emps)
        avg_p = Payroll.calculate_average_projects(emps)
        for row in report:
            self.txt_pay.insert(
                tk.END,
                f"[{row['type']}] {row['id']} — {row['name']}: {Formatters.format_currency(row['salary'])}\n",
            )
        self.txt_pay.insert(tk.END, f"\nTrung bình số dự án / người: {avg_p:.2f}\n")

    def _tab_project_management(self, nb):
        tab = ttk.Frame(nb, padding=12)
        nb.add(tab, text="Quản lý dự án")

        sf = ttk.LabelFrame(tab, text="Nhân viên theo số dự án tham gia (nhiều → ít)", padding=10)
        sf.pack(fill=tk.BOTH, expand=True, pady=(0, 8))

        bar = ttk.Frame(sf)
        bar.pack(fill=tk.X, pady=(0, 6))
        ttk.Label(bar, text="Sắp xếp theo số lượng dự án giảm dần.", foreground="gray").pack(side=tk.LEFT)
        ttk.Button(bar, text="Làm mới", command=self._refresh_project_count_tree).pack(side=tk.RIGHT)

        cols = ("id", "name", "kind", "nproj", "tenure", "projects")
        self.tree_proj_count = ttk.Treeview(sf, columns=cols, show="headings", height=10)
        heads = {
            "id": "Mã ID",
            "name": "Họ tên",
            "kind": "Loại",
            "nproj": "Số dự án",
            "tenure": "Thâm niên (tháng)",
            "projects": "Các dự án",
        }
        w = {"id": 85, "name": 140, "kind": 85, "nproj": 75, "tenure": 110, "projects": 280}
        for c in cols:
            self.tree_proj_count.heading(c, text=heads[c])
            self.tree_proj_count.column(c, width=w[c], anchor=tk.W)

        sy = ttk.Scrollbar(sf, orient=tk.VERTICAL, command=self.tree_proj_count.yview)
        self.tree_proj_count.configure(yscrollcommand=sy.set)
        self.tree_proj_count.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        sy.pack(side=tk.RIGHT, fill=tk.Y)

        af = ttk.LabelFrame(tab, text="Danh sách dự án & nhân viên tham gia", padding=10)
        af.pack(fill=tk.BOTH, expand=True, pady=(0, 8))
        ttk.Button(af, text="Làm mới danh sách", command=self._refresh_project_mgmt_roster).pack(anchor=tk.E, pady=(0, 6))
        self.txt_mgmt_roster = scrolledtext.ScrolledText(af, height=8, wrap=tk.WORD, font=("Consolas", 10))
        self.txt_mgmt_roster.pack(fill=tk.BOTH, expand=True)

        cf = ttk.LabelFrame(tab, text="Đền bù / thưởng milestone theo dự án (xem công thức trong compensation.py)", padding=10)
        cf.pack(fill=tk.X)
        self.var_comp_emp_id = tk.StringVar()
        self.var_comp_proj = tk.StringVar()
        ttk.Label(cf, text="Mã NV:").grid(row=0, column=0, sticky=tk.W, padx=(0, 8))
        ttk.Entry(cf, textvariable=self.var_comp_emp_id, width=18).grid(row=0, column=1, sticky=tk.W)
        ttk.Label(cf, text="Tên dự án:").grid(row=0, column=2, sticky=tk.W, padx=(12, 8))
        ttk.Entry(cf, textvariable=self.var_comp_proj, width=28).grid(row=0, column=3, sticky=tk.W)
        ttk.Button(cf, text="Tính đền bù dự án", command=self._calc_project_compensation).grid(
            row=1, column=1, pady=(8, 0), sticky=tk.W
        )
        self.txt_comp_hint = ttk.Label(
            cf,
            text="Áp dụng khi nhân viên đang gắn với dự án đó. Kết quả hiển thị bên dưới.",
            foreground="gray",
        )
        self.txt_comp_hint.grid(row=1, column=2, columnspan=2, sticky=tk.W, pady=(8, 0), padx=(12, 0))
        self.txt_comp_result = scrolledtext.ScrolledText(tab, height=4, wrap=tk.WORD, font=("Consolas", 10))
        self.txt_comp_result.pack(fill=tk.X, pady=(8, 0))

    def _refresh_project_count_tree(self):
        if not hasattr(self, "tree_proj_count"):
            return
        for i in self.tree_proj_count.get_children():
            self.tree_proj_count.delete(i)
        for emp in self.company.get_employees_sorted_by_project_count():
            plist = ", ".join(emp.projects) if emp.projects else "—"
            self.tree_proj_count.insert(
                "",
                tk.END,
                values=(
                    emp.emp_id,
                    emp.name,
                    emp.__class__.__name__,
                    len(emp.projects),
                    emp.tenure_months,
                    plist,
                ),
            )

    def _refresh_project_mgmt_roster(self):
        if not hasattr(self, "txt_mgmt_roster"):
            return
        self.txt_mgmt_roster.delete("1.0", tk.END)
        roster = self.company.get_projects_with_members()
        if not roster:
            self.txt_mgmt_roster.insert(tk.END, "Chưa có dự án nào.\n")
            return
        for pname, members in roster.items():
            self.txt_mgmt_roster.insert(tk.END, f"{pname}\n")
            for emp in members:
                self.txt_mgmt_roster.insert(
                    tk.END,
                    f"  • {emp.name}  ({emp.emp_id})  [{emp.__class__.__name__}]\n",
                )
            self.txt_mgmt_roster.insert(tk.END, "\n")

    def _calc_project_compensation(self):
        self.txt_comp_result.delete("1.0", tk.END)
        try:
            emp = self.company.find_employee_by_id(self.var_comp_emp_id.get().strip())
            pname = self.var_comp_proj.get().strip()
            amt = Compensation.calculate_project_compensation(emp, pname)
            self.txt_comp_result.insert(
                tk.END,
                f"Nhân viên: {emp.name} ({emp.emp_id})\nDự án: {pname}\n"
                f"Đền bù / thưởng milestone (dự kiến): {Formatters.format_currency(amt)}\n",
            )
        except EmployeeError as e:
            messagebox.showerror("Lỗi", str(e))
        except ValueError as e:
            messagebox.showerror("Lỗi", str(e))

    def _tab_hr(self, nb):
        tab = ttk.Frame(nb, padding=12)
        nb.add(tab, text="Quản lý nhân sự")

        rf = ttk.LabelFrame(tab, text="Giảm lương cơ bản", padding=10)
        rf.pack(fill=tk.X, pady=(0, 8))
        self.var_hr_down_id = tk.StringVar()
        self.var_hr_down_amt = tk.StringVar()
        ttk.Label(rf, text="Mã NV:").grid(row=0, column=0, sticky=tk.W, padx=(0, 8))
        ttk.Entry(rf, textvariable=self.var_hr_down_id, width=22).grid(row=0, column=1, sticky=tk.W)
        ttk.Label(rf, text="Số tiền giảm (VNĐ):").grid(row=0, column=2, sticky=tk.W, padx=(12, 8))
        ttk.Entry(rf, textvariable=self.var_hr_down_amt, width=22).grid(row=0, column=3, sticky=tk.W)
        ttk.Button(rf, text="Áp dụng giảm lương", command=self._hr_reduce_salary).grid(
            row=1, column=1, pady=(8, 0), sticky=tk.W
        )

        xf = ttk.LabelFrame(tab, text="Nghỉ việc & đền bù hợp đồng", padding=10)
        xf.pack(fill=tk.X, pady=(0, 8))
        self.var_hr_resign_id = tk.StringVar()
        ttk.Label(xf, text="Mã NV:").grid(row=0, column=0, sticky=tk.W, padx=(0, 8))
        ttk.Entry(xf, textvariable=self.var_hr_resign_id, width=22).grid(row=0, column=1, sticky=tk.W)
        ttk.Button(xf, text="Xem trước đền bù", command=self._hr_preview_severance).grid(row=0, column=2, padx=8)
        ttk.Button(xf, text="Xác nhận nghỉ việc (có đền bù)", command=self._hr_resign).grid(row=0, column=3, padx=8)
        ttk.Label(
            xf,
            text="Xác nhận sẽ ghi log, xóa nhân viên khỏi danh sách đang làm việc.",
            foreground="gray",
        ).grid(row=1, column=0, columnspan=4, sticky=tk.W, pady=(8, 0))

        lf = ttk.LabelFrame(tab, text="Lịch sử nghỉ việc (đền bù đã chi trong phiên làm việc)", padding=10)
        lf.pack(fill=tk.BOTH, expand=True)
        ttk.Button(lf, text="Làm mới", command=self._refresh_resign_log).pack(anchor=tk.E, pady=(0, 6))
        self.txt_resign_log = scrolledtext.ScrolledText(lf, height=12, wrap=tk.WORD, font=("Consolas", 10))
        self.txt_resign_log.pack(fill=tk.BOTH, expand=True)

    def _hr_reduce_salary(self):
        try:
            emp = self.company.find_employee_by_id(self.var_hr_down_id.get().strip())
            cut = float(self.var_hr_down_amt.get().strip().replace(",", ""))
            if cut <= 0:
                raise ValueError("Số tiền giảm phải lớn hơn 0.")
            new_sal = emp.base_salary - cut
            Validators.validate_salary(new_sal)
            emp.base_salary = new_sal
            messagebox.showinfo("OK", f"Lương CB mới: {Formatters.format_currency(new_sal)}")
            self._refresh_all()
        except EmployeeError as e:
            messagebox.showerror("Lỗi", str(e))
        except ValueError as e:
            messagebox.showerror("Lỗi", str(e))

    def _hr_preview_severance(self):
        try:
            emp = self.company.find_employee_by_id(self.var_hr_resign_id.get().strip())
            amt = Compensation.calculate_contract_severance(emp)
            messagebox.showinfo(
                "Xem trước đền bù",
                f"{emp.name} ({emp.emp_id})\n"
                f"Thâm niên: {emp.tenure_months} tháng\n"
                f"Đền bù hợp đồng (dự kiến): {Formatters.format_currency(amt)}",
            )
        except EmployeeError as e:
            messagebox.showerror("Lỗi", str(e))

    def _hr_resign(self):
        try:
            eid = self.var_hr_resign_id.get().strip()
            emp = self.company.find_employee_by_id(eid)
            prev = Compensation.calculate_contract_severance(emp)
            if not messagebox.askyesno(
                "Nghỉ việc",
                f"Đền bù hợp đồng (dự kiến): {Formatters.format_currency(prev)}\n"
                f"Xác nhận nghỉ việc và xóa khỏi danh sách nhân viên đang làm việc?",
            ):
                return
            amt = self.company.resign_with_severance(eid)
            messagebox.showinfo("Hoàn tất", f"Đã ghi nhận nghỉ việc.\nĐền bù: {Formatters.format_currency(amt)}")
            self._refresh_all()
        except EmployeeError as e:
            messagebox.showerror("Lỗi", str(e))

    def _refresh_resign_log(self):
        if not hasattr(self, "txt_resign_log"):
            return
        self.txt_resign_log.delete("1.0", tk.END)
        if not self.company.resignation_log:
            self.txt_resign_log.insert(tk.END, "Chưa có bản ghi nghỉ việc trong phiên này.\n")
            return
        for rec in reversed(self.company.resignation_log):
            self.txt_resign_log.insert(
                tk.END,
                f"{rec['date']} | {rec['emp_id']} | {rec['name']} | "
                f"{Formatters.format_currency(rec['severance'])}\n",
            )

    def _refresh_all(self):
        self._refresh_tree()
        self._refresh_project_roster()
        self._refresh_project_count_tree()
        self._refresh_project_mgmt_roster()
        self._refresh_resign_log()

    def _tab_performance_projects(self, nb):
        tab = ttk.Frame(nb, padding=12)
        nb.add(tab, text="Hiệu suất & dự án")

        pf = ttk.LabelFrame(tab, text="Cập nhật điểm hiệu suất (0–10)", padding=10)
        pf.pack(fill=tk.X, pady=(0, 8))
        self.var_perf_id = tk.StringVar()
        self.var_perf_score = tk.StringVar()
        ttk.Label(pf, text="Mã nhân viên:").grid(row=0, column=0, sticky=tk.W, padx=(0, 8))
        ttk.Entry(pf, textvariable=self.var_perf_id, width=24).grid(row=0, column=1, sticky=tk.W)
        ttk.Label(pf, text="Điểm:").grid(row=0, column=2, sticky=tk.W, padx=(12, 8))
        ttk.Entry(pf, textvariable=self.var_perf_score, width=12).grid(row=0, column=3, sticky=tk.W)
        ttk.Button(pf, text="Cập nhật", command=self._update_perf).grid(row=0, column=4, padx=(12, 0))

        jf = ttk.LabelFrame(tab, text="Dự án (tối đa 5 / người)", padding=10)
        jf.pack(fill=tk.X, pady=(0, 8))
        self.var_proj_id = tk.StringVar()
        self.var_proj_name = tk.StringVar()
        ttk.Label(jf, text="Mã NV:").grid(row=0, column=0, sticky=tk.W, padx=(0, 8))
        ttk.Entry(jf, textvariable=self.var_proj_id, width=20).grid(row=0, column=1, sticky=tk.W)
        ttk.Label(jf, text="Tên dự án:").grid(row=0, column=2, sticky=tk.W, padx=(12, 8))
        ttk.Entry(jf, textvariable=self.var_proj_name, width=28).grid(row=0, column=3, sticky=tk.W)
        ttk.Button(jf, text="Gán dự án", command=self._add_project).grid(row=1, column=1, pady=(8, 0), sticky=tk.W)
        ttk.Button(jf, text="Xóa khỏi dự án", command=self._remove_project).grid(row=1, column=3, pady=(8, 0), sticky=tk.W)

        allp = ttk.LabelFrame(tab, text="Tất cả dự án — thành viên tham gia", padding=10)
        allp.pack(fill=tk.BOTH, expand=True, pady=(0, 8))
        barp = ttk.Frame(allp)
        barp.pack(fill=tk.X, pady=(0, 6))
        ttk.Label(
            barp,
            text="Mỗi dự án liệt kê nhân viên đang được gán.",
            foreground="gray",
        ).pack(side=tk.LEFT)
        ttk.Button(barp, text="Làm mới", command=self._refresh_all).pack(side=tk.RIGHT)
        self.txt_proj_roster = scrolledtext.ScrolledText(allp, height=12, wrap=tk.WORD, font=("Consolas", 10))
        self.txt_proj_roster.pack(fill=tk.BOTH, expand=True)

        lf = ttk.LabelFrame(tab, text="Danh sách dự án theo nhân viên", padding=10)
        lf.pack(fill=tk.X)
        self.var_list_proj_id = tk.StringVar()
        ttk.Label(lf, text="Mã NV:").pack(side=tk.LEFT, padx=(0, 8))
        ttk.Entry(lf, textvariable=self.var_list_proj_id, width=20).pack(side=tk.LEFT, padx=(0, 8))
        ttk.Button(lf, text="Hiển thị", command=self._list_projects).pack(side=tk.LEFT)

        self.txt_proj = scrolledtext.ScrolledText(tab, height=8, wrap=tk.WORD, font=("Consolas", 10))
        self.txt_proj.pack(fill=tk.BOTH, expand=True, pady=(8, 0))

    def _refresh_project_roster(self):
        if not hasattr(self, "txt_proj_roster"):
            return
        self.txt_proj_roster.delete("1.0", tk.END)
        roster = self.company.get_projects_with_members()
        if not roster:
            self.txt_proj_roster.insert(tk.END, "Chưa có dự án nào trong hệ thống.\n")
            return
        for pname, members in roster.items():
            self.txt_proj_roster.insert(tk.END, f"{pname}\n")
            for emp in members:
                self.txt_proj_roster.insert(
                    tk.END,
                    f"  • {emp.name}  ({emp.emp_id})  [{emp.__class__.__name__}]\n",
                )
            self.txt_proj_roster.insert(tk.END, "\n")

    def _update_perf(self):
        try:
            emp = self.company.find_employee_by_id(self.var_perf_id.get().strip())
            score = float(self.var_perf_score.get().strip().replace(",", "."))
            emp.performance_score = score
            messagebox.showinfo("OK", "Đã cập nhật điểm hiệu suất.")
            self._refresh_all()
        except EmployeeError as e:
            messagebox.showerror("Lỗi", str(e))
        except ValueError as e:
            messagebox.showerror("Lỗi", str(e))

    def _add_project(self):
        try:
            emp = self.company.find_employee_by_id(self.var_proj_id.get().strip())
            emp.add_project(self.var_proj_name.get().strip())
            messagebox.showinfo("OK", "Đã gán dự án.")
            self._refresh_all()
        except EmployeeError as e:
            messagebox.showerror("Lỗi", str(e))

    def _remove_project(self):
        try:
            emp = self.company.find_employee_by_id(self.var_proj_id.get().strip())
            emp.remove_project(self.var_proj_name.get().strip())
            messagebox.showinfo("OK", "Đã xóa dự án khỏi danh sách.")
            self._refresh_all()
        except EmployeeError as e:
            messagebox.showerror("Lỗi", str(e))

    def _list_projects(self):
        self.txt_proj.delete("1.0", tk.END)
        try:
            emp = self.company.find_employee_by_id(self.var_list_proj_id.get().strip())
            if not emp.projects:
                self.txt_proj.insert(tk.END, "Chưa có dự án nào.\n")
                return
            for p in emp.projects:
                self.txt_proj.insert(tk.END, f"• {p}\n")
        except EmployeeError as e:
            messagebox.showwarning("Lỗi", str(e))

    def _tab_remove(self, nb):
        tab = ttk.Frame(nb, padding=12)
        nb.add(tab, text="Xóa nhân viên")

        f = ttk.Frame(tab)
        f.pack(anchor=tk.W)
        self.var_del_id = tk.StringVar()
        ttk.Label(f, text="Mã nhân viên cần xóa:").pack(side=tk.LEFT, padx=(0, 8))
        ttk.Entry(f, textvariable=self.var_del_id, width=28).pack(side=tk.LEFT, padx=(0, 8))
        ttk.Button(f, text="Xóa", command=self._remove_emp).pack(side=tk.LEFT)

        ttk.Label(
            tab,
            text="Thao tác không thể hoàn tác. Hệ thống sẽ xác nhận trước khi xóa.",
            foreground="gray",
        ).pack(anchor=tk.W, pady=(16, 0))

    def _remove_emp(self):
        eid = self.var_del_id.get().strip()
        if not eid:
            return
        if not messagebox.askyesno("Xác nhận", f"Bạn chắc chắn muốn xóa nhân viên {eid}?"):
            return
        try:
            self.company.remove_employee(eid)
            messagebox.showinfo("OK", "Đã xóa nhân viên.")
            self._refresh_all()
        except EmployeeError as e:
            messagebox.showerror("Lỗi", str(e))

    def run(self):
        self._refresh_all()
        self.root.mainloop()


def main():
    app = EmployeeManagementGUI()
    app.run()


if __name__ == "__main__":
    main()
