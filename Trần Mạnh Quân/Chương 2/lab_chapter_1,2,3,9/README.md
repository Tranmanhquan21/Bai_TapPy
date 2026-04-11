# Hệ thống quản lý nhân viên — Công ty ABC

Ứng dụng desktop quản lý nhân sự: nhân viên theo loại (Manager / Developer / Intern), lương, dự án, hiệu suất, **đền bù hợp đồng / đền bù dự án**, giảm lương và nghỉ việc có ghi log. Xây dựng bằng **Python 3.8+**, giao diện **Tkinter** (thư viện chuẩn), **OOP** (kế thừa, đa hình, ngoại lệ tùy chỉnh).

## Tổng quan

| Hạng mục | Nội dung |
|----------|----------|
| Giao diện | Cửa sổ nhiều tab (Notebook) |
| Dữ liệu | Chỉ trong RAM khi chạy; có **dữ liệu mẫu** lúc khởi động |
| Phụ thuộc | Không cần `pip install` thêm (Python + Tkinter) |

## Các tab trong ứng dụng

1. **Thêm nhân viên** — Chọn loại; nhập ID, tên, tuổi, lương CB, **thâm niên (tháng)**; thông tin riêng: quy mô team / ngôn ngữ / chuyên ngành. Kiểm tra tuổi, lương.
2. **Danh sách** — Bảng nhân viên; lọc theo loại hoặc sắp theo điểm hiệu suất (cao → thấp).
3. **Tìm kiếm** — Theo mã ID hoặc tên (chuỗi con).
4. **Lương & thống kê** — Tổng quỹ lương, top 3 lương cao, báo cáo chi tiết + trung bình số dự án/người (`Payroll`).
5. **Quản lý dự án** — Bảng **sắp nhân viên theo số dự án (nhiều → ít)**; danh sách **từng dự án và người tham gia**; tính **đền bù / thưởng milestone theo một dự án** (`Compensation`).
6. **Hiệu suất & dự án** — Cập nhật điểm 0–10; gán / gỡ dự án (tối đa 5/người); xem tất cả dự án — thành viên; xem dự án theo mã nhân viên.
7. **Quản lý nhân sự** — **Giảm lương cơ bản**; **nghỉ việc kèm đền bù hợp đồng** (xem trước / xác nhận); **lịch sử nghỉ việc** trong phiên.
8. **Xóa nhân viên** — Xóa nhanh khỏi hệ thống (có xác nhận), **không** tính đền bù như tab Quản lý nhân sự.

**Dữ liệu mẫu** (`sample_data.py`): nạp 7 nhân viên kèm điểm, dự án và **thâm niên** khác nhau (chỉ khi danh sách đang trống).

## Cấu trúc thư mục

```
lab_chapter_1,2,3,9/
├── README.md
├── GIAI_THICH_CODE.txt
└── employee_management/
    ├── main.py                 # Giao diện Tkinter + điểm vào
    ├── sample_data.py
    ├── models/
    │   ├── employee.py         # Abstract + tenure_months, projects, …
    │   ├── manager.py
    │   ├── developer.py
    │   └── intern.py
    ├── services/
    │   ├── company.py          # CRUD, thống kê, dự án, nghỉ việc + log
    │   ├── payroll.py          # Báo cáo lương, trung bình dự án
    │   └── compensation.py   # Đền bù HĐLĐ + đền bù theo dự án
    ├── utils/
    │   ├── validators.py
    │   └── formatters.py
    └── exceptions/
        └── employee_exceptions.py
```

## Cách chạy

```bash
cd employee_management
python main.py
```

Đóng cửa sổ để thoát.

## Quy tắc nghiệp vụ (tóm tắt)

| Nội dung | Chi tiết |
|----------|----------|
| Tuổi | 18–65 (`InvalidAgeError`) |
| Lương CB | Phải dương (`InvalidSalaryError`); sau giảm lương vẫn phải hợp lệ |
| Điểm hiệu suất | 0–10 khi gán |
| Dự án | Tối đa 5/người (`ProjectAllocationError`) |
| ID trùng | `DuplicateEmployeeError` |
| Không tìm thấy | `EmployeeNotFoundError` |
| Đền bù theo dự án | Tên dự án phải trùng với tên trong danh sách dự án của nhân viên |

Công thức **đền bù** (hợp đồng / dự án) được mô tả trong `services/compensation.py`.

## OOP

- Kế thừa: `Employee` → `Manager`, `Developer`, `Intern`
- Đa hình: `calculate_salary()` mỗi lớp một cách tính
- Trừu tượng: `calculate_salary` abstract trên `Employee`
- Đóng gói: property, giới hạn điểm hiệu suất, quản lý dự án trên từng đối tượng

## Tác giả & giấy phép

**Tác giả:** Trần Mạnh Quân  

MIT License — tự do sử dụng và chỉnh sửa.
