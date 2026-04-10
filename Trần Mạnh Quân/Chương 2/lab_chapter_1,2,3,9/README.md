# MÔ TẢ BÀI TOÁN: HỆ THỐNG QUẢN LÝ NHÂN VIÊN CÔNG TY ABC

## 1. Tổng quan
Xây dựng một hệ thống quản lý nhân viên (Employee Management System) nhằm tối ưu hóa việc theo dõi thông tin, tính lương, phân công công việc và đánh giá hiệu suất của nhân sự trong công ty. Hệ thống được thiết kế theo mô hình hướng đối tượng (OOP) và cấu trúc module hóa để dễ dàng bảo trì và mở rộng.

## 2. Các chức năng chính

### 2.1. Quản lý thông tin nhân viên
*   **Thêm nhân viên mới**: Cho phép thêm các loại nhân viên khác nhau:
    *   **Manager (Quản lý)**: Có thêm thông tin về số lượng nhân viên dưới quyền.
    *   **Developer (Lập trình viên)**: Có thêm thông tin về ngôn ngữ lập trình sử dụng.
    *   **Intern (Thực tập sinh)**: Có thông tin về chuyên ngành và thời gian thực tập.
*   **Hiển thị danh sách**:
    *   Xem tất cả nhân viên.
    *   Lọc theo loại nhân viên.
    *   Sắp xếp theo hiệu suất làm việc (từ cao đến thấp).
*   **Tìm kiếm**:
    *   Tìm kiếm theo ID hoặc Tên.
    *   Tìm kiếm Developer theo ngôn ngữ lập trình.

### 2.2. Tính lương và Thống kê
*   **Tính lương**: Tính toán lương cho từng cá nhân và tổng lương toàn công ty dựa trên chức vụ và hiệu suất.
*   **Vinh danh**: Hiển thị Top 3 nhân viên có mức lương cao nhất.
*   **Thống kê**:
    *   Số lượng nhân viên theo từng loại.
    *   Tổng quỹ lương theo từng phòng ban.
    *   Số dự án trung bình mỗi nhân viên tham gia.

### 2.3. Quản lý Dự án và Hiệu suất
*   **Dự án**:
    *   Phân công nhân viên vào các dự án cụ thể.
    *   Xóa nhân viên khỏi dự án.
    *   Xem danh sách dự án của một nhân viên.
*   **Hiệu suất**:
    *   Cập nhật điểm hiệu suất cho nhân viên (thang điểm 10).
    *   Phân loại nhân viên xuất sắc (điểm > 8) và nhân viên cần cải thiện (điểm < 5).

### 2.4. Quản lý Nhân sự nâng cao
*   Xóa nhân viên khi họ nghỉ việc.
*   Tăng lương cơ bản cho nhân viên.
*   Thăng chức cho nhân viên (Intern -> Developer -> Manager).

## 3. Cấu trúc Project (Dự kiến)
Hệ thống sẽ được tổ chức theo cấu trúc package:
*   `main.py`: Chương trình chính, hiển thị menu tương tác.
*   `models/`: Chứa các lớp `Employee` (lớp cơ sở), `Manager`, `Developer`, `Intern`.
*   `services/`: Chứa logic nghiệp vụ (`Company` quản lý danh sách, `Payroll` xử lý lương).
*   `utils/`: Chứa các công cụ hỗ trợ (`Validators` kiểm tra dữ liệu, `Formatters` định dạng hiển thị).
*   `exceptions/`: Định nghĩa các ngoại lệ tùy chỉnh.

## 4. Xử lý lỗi đầu vào (Exception Handling)
Hệ thống cần xử lý các trường hợp ngoại lệ để đảm bảo tính ổn định:
*   **Dữ liệu cá nhân**: Tuổi không hợp lệ (ngoài 18-65), Lương <= 0, Email sai định dạng.
*   **Quản lý ID**: ID không tồn tại hoặc ID bị trùng lặp khi thêm mới.
*   **Ràng buộc nghiệp vụ**: Nhân viên đã tham gia tối đa 5 dự án, cập nhật điểm ngoài khoảng 0-10.
*   **Trạng thái hệ thống**: Truy cập danh sách rỗng, nhập sai lựa chọn menu.
