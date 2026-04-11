# Hệ thống quản lý nhân viên — Công ty ABC

Ứng dụng desktop quản lý nhân sự: thêm/sửa thông tin, tính lương theo loại nhân viên và hiệu suất, phân công dự án, thống kê. Xây dựng bằng **Python 3.8+**, giao diện **Tkinter** (thư viện chuẩn), mô hình **OOP** (kế thừa, đa hình, ngoại lệ tùy chỉnh).

## Tổng quan

| Hạng mục | Nội dung |
|----------|----------|
| Giao diện | Cửa sổ với các tab chức năng |
| Dữ liệu | Lưu trong bộ nhớ khi chạy; có **dữ liệu mẫu** khi khởi động |
| Phụ thuộc | Không cần `pip install` thêm (chỉ Python + Tkinter) |

## Chức năng trong ứng dụng

1. **Thêm nhân viên** — Chọn loại: Manager (quy mô team), Developer (ngôn ngữ), Intern (chuyên ngành); kiểm tra tuổi và lương cơ bản.
2. **Danh sách** — Bảng nhân viên; lọc theo loại hoặc sắp xếp theo điểm hiệu suất (cao → thấp).
3. **Tìm kiếm** — Theo mã ID hoặc theo tên (chuỗi con).
4. **Lương & thống kê** — Tổng quỹ lương, top 3 lương cao, báo cáo chi tiết và trung bình số dự án trên mỗi người (`Payroll`).
5. **Hiệu suất & dự án** — Cập nhật điểm 0–10; gán / gỡ dự án (tối đa 5 dự án/người); xem danh sách dự án theo nhân viên.
6. **Xóa nhân viên** — Có xác nhận trước khi xóa.

**Dữ liệu mẫu:** file `sample_data.py` nạp sẵn một số Manager, Developer, Intern kèm điểm hiệu suất và vài dự án (chỉ khi danh sách đang trống).

## Cấu trúc thư mục

```
lab_chapter_1,2,3,9/
└── employee_management/
    ├── main.py                 # Giao diện Tkinter + điểm vào chương trình
    ├── sample_data.py          # Dữ liệu mẫu (seed)
    ├── models/
    │   ├── employee.py         # Lớp cơ sở (abstract)
    │   ├── manager.py
    │   ├── developer.py
    │   └── intern.py
    ├── services/
    │   ├── company.py          # Danh sách, tìm kiếm, tổng lương, top 3, …
    │   └── payroll.py          # Báo cáo lương, trung bình dự án
    ├── utils/
    │   ├── validators.py       # Tuổi, lương, email (regex)
    │   └── formatters.py       # Định dạng tiền tệ, tiêu đề
    └── exceptions/
        └── employee_exceptions.py
```

## Cách chạy

Trong thư mục `employee_management`:

```bash
cd employee_management
python main.py
```

Đóng cửa sổ để thoát chương trình.

## Quy tắc nghiệp vụ & lỗi thường gặp

| Nội dung | Chi tiết |
|----------|----------|
| Tuổi | Từ 18 đến 65 (`InvalidAgeError`) |
| Lương cơ bản | Phải là số dương (`InvalidSalaryError`) |
| Điểm hiệu suất | 0–10; ngoài khoảng sẽ báo lỗi khi gán |
| Dự án | Tối đa 5 dự án mỗi người (`ProjectAllocationError`) |
| ID trùng | Không cho thêm ID đã tồn tại (`DuplicateEmployeeError`) |
| Không tìm thấy | ID hoặc tên không khớp (`EmployeeNotFoundError`) |

Thông báo lỗi khi thao tác trên GUI hiển thị qua hộp thoại (`messagebox`).

## OOP trong project

- **Kế thừa:** `Employee` → `Manager`, `Developer`, `Intern`
- **Đa hình:** `calculate_salary()` triển khai khác nhau theo lớp
- **Trừu tượng:** phương thức trừu tượng trên lớp cơ sở
- **Đóng gói:** thuộc tính và truy cập qua property/setter phù hợp

## Tác giả & giấy phép

**Tác giả:** Trần Mạnh Quân  

MIT License — tự do sử dụng và chỉnh sửa.
