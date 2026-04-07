class HocVien:
    # a) Tạo class với các thuộc tính tương ứng
    def __init__(self, ho_ten, ngay_sinh, email, dien_thoai, dia_chi, lop):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.email = email
        self.dien_thoai = dien_thoai
        self.dia_chi = dia_chi
        self.lop = lop

    # b) Tạo phương thức show_info trả về đầy đủ thông tin
    def show_info(self):
        info = (
            f"--- Thông tin học viên ---\n"
            f"Họ tên: {self.ho_ten}\n"
            f"Ngày sinh: {self.ngay_sinh}\n"
            f"Email: {self.email}\n"
            f"Điện thoại: {self.dien_thoai}\n"
            f"Địa chỉ: {self.dia_chi}\n"
            f"Lớp: {self.lop}\n"
        )
        return info

    # c) Tạo phương thức change_info với tham số mặc định
    def change_info(self, dia_chi='Hà Nội', lop='IT12.x'):
        self.dia_chi = dia_chi
        self.lop = lop
        print(f"==> Đã cập nhật thông tin cho học viên {self.ho_ten} thành công!")

# d) Chương trình chính
if __name__ == "__main__":
    # Tạo đối tượng học viên mới
    hv1 = HocVien(
        ho_ten="Nguyễn Văn A", 
        ngay_sinh="20/05/2000", 
        email="vana@gmail.com", 
        dien_thoai="0987654321", 
        dia_chi="Đà Nẵng", 
        lop="IT10.1"
    )

    # Gọi phương thức show_info để xem thông tin ban đầu
    print(hv1.show_info())

    # Gọi phương thức change_info (sử dụng giá trị mặc định: Hà Nội và IT12.x)
    hv1.change_info()

    # Gọi lại show_info để kiểm tra thay đổi
    print(hv1.show_info())

    # Thử thay đổi với giá trị tùy biến khác
    hv1.change_info(dia_chi="TP.HCM", lop="Python_Pro")
    print(hv1.show_info())