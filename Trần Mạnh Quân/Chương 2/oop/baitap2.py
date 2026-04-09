import math

class PhanSo:
    def __init__(self, tu_so, mau_so=1):
        """
        Khởi tạo phân số với tử số và mẫu số.
        Mặc định mẫu số bằng 1. Thông báo lỗi nếu mẫu số bằng 0.
        """
        if mau_so == 0:
            raise ValueError("Lỗi: Mẫu số không được bằng 0.")
        self.tu_so = tu_so
        self.mau_so = mau_so

    def __str__(self):
        """Trả về chuỗi đại diện cho phân số (ví dụ: '1/2')."""
        if self.mau_so == 1:
            return str(self.tu_so)
        return f"{self.tu_so}/{self.mau_so}"

    def toi_gian(self):
        """Rút gọn phân số về dạng tối giản."""
        common = math.gcd(self.tu_so, self.mau_so)
        self.tu_so //= common
        self.mau_so //= common
        
        # Đảm bảo mẫu số luôn dương để hiển thị đẹp hơn
        if self.mau_so < 0:
            self.tu_so = -self.tu_so
            self.mau_so = -self.mau_so
        return self

    def tong(self, ps2):
        """Cộng phân số hiện tại với phân số ps2."""
        tu = self.tu_so * ps2.mau_so + ps2.tu_so * self.mau_so
        mau = self.mau_so * ps2.mau_so
        return PhanSo(tu, mau).toi_gian()

    def hieu(self, ps2):
        """Trừ phân số hiện tại cho phân số ps2."""
        tu = self.tu_so * ps2.mau_so - ps2.tu_so * self.mau_so
        mau = self.mau_so * ps2.mau_so
        return PhanSo(tu, mau).toi_gian()

    def nhan(self, ps2):
        """Nhân phân số hiện tại với phân số ps2."""
        tu = self.tu_so * ps2.tu_so
        mau = self.mau_so * ps2.mau_so
        return PhanSo(tu, mau).toi_gian()

    def chia(self, ps2):
        """Chia phân số hiện tại cho phân số ps2."""
        if ps2.tu_so == 0:
            raise ValueError("Lỗi: Không thể chia cho phân số có tử số bằng 0.")
        tu = self.tu_so * ps2.mau_so
        mau = self.mau_so * ps2.tu_so
        return PhanSo(tu, mau).toi_gian()

# --- Chạy thử nghiệm các tính năng ---
if __name__ == "__main__":
    print("--- Chương trình tính toán Phân Số ---")
    
    try:
        # Nhập phân số 1
        print("\nNhập phân số thứ nhất:")
        t1 = int(input("  Tử số: "))
        m1 = int(input("  Mẫu số: "))
        ps1 = PhanSo(t1, m1)
        
        # Nhập phân số 2
        print("\nNhập phân số thứ hai:")
        t2 = int(input("  Tử số: "))
        m2 = int(input("  Mẫu số: "))
        ps2 = PhanSo(t2, m2)
        
        print("\n" + "="*30)
        print(f"Phân số 1: {ps1}")
        print(f"Phân số 2: {ps2}")
        print("="*30)
        
        # Thực hiện các phép tính
        print(f"Tổng:  {ps1} + {ps2} = {ps1.tong(ps2)}")
        print(f"Hiệu:  {ps1} - {ps2} = {ps1.hieu(ps2)}")
        print(f"Nhân:  {ps1} * {ps2} = {ps1.nhan(ps2)}")
        
        try:
            print(f"Chia:  {ps1} / {ps2} = {ps1.chia(ps2)}")
        except ValueError as e:
            print(f"Chia:  Lỗi ({e})")
            
        # Thử nghiệm tối giản một phân số bất kỳ
        print("\n--- Thử nghiệm tối giản ---")
        t3 = int(input("Nhập tử số cần tối giản: "))
        m3 = int(input("Nhập mẫu số cần tối giản: "))
        ps3 = PhanSo(t3, m3)
        print(f"Trước tối giản: {ps3}")
        ps3.toi_gian()
        print(f"Sau tối giản:   {ps3}")
        
    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên hợp lệ.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
