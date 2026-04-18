import sqlite3

# Tên file cơ sở dữ liệu
DB_NAME = 'database_nhansu.db'

def ket_noi_db():
    """Tạo và trả về kết nối đến CSDL SQLite."""
    return sqlite3.connect(DB_NAME)

def tao_bang_neu_chua_co():
    """Tạo bảng NhanSu nếu chưa tồn tại trong CSDL."""
    conn = ket_noi_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS NhanSu (
            cccd TEXT PRIMARY KEY,
            ho_ten TEXT NOT NULL,
            ngay_sinh TEXT,
            gioi_tinh TEXT,
            dia_chi TEXT
        )
    ''')
    conn.commit()
    conn.close()

def them_nhan_su(cccd, ho_ten, ngay_sinh, gioi_tinh, dia_chi):
    conn = ket_noi_db()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO NhanSu (cccd, ho_ten, ngay_sinh, gioi_tinh, dia_chi)
            VALUES (?, ?, ?, ?, ?)
        ''', (cccd, ho_ten, ngay_sinh, gioi_tinh, dia_chi))
        conn.commit()
        print(f"\n[+] Đã thêm thành công nhân sự: {ho_ten}")
    except sqlite3.IntegrityError:
        print(f"\n[!] Lỗi: Số CCCD '{cccd}' đã tồn tại trong hệ thống!")
    finally:
        conn.close()

def sua_nhan_su(cccd, ho_ten, ngay_sinh, gioi_tinh, dia_chi):
    conn = ket_noi_db()
    cursor = conn.cursor()
    
    # Kiểm tra xem CCCD có tồn tại không
    cursor.execute('SELECT * FROM NhanSu WHERE cccd = ?', (cccd,))
    if not cursor.fetchone():
        print(f"\n[!] Không tìm thấy nhân sự có số CCCD: {cccd}")
        conn.close()
        return

    cursor.execute('''
        UPDATE NhanSu 
        SET ho_ten = ?, ngay_sinh = ?, gioi_tinh = ?, dia_chi = ?
        WHERE cccd = ?
    ''', (ho_ten, ngay_sinh, gioi_tinh, dia_chi, cccd))
    conn.commit()
    print(f"\n[+] Đã cập nhật thành công thông tin cho CCCD: {cccd}")
    conn.close()

def xoa_nhan_su(cccd):
    conn = ket_noi_db()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM NhanSu WHERE cccd = ?', (cccd,))
    if not cursor.fetchone():
        print(f"\n[!] Không tìm thấy nhân sự có số CCCD: {cccd}")
        conn.close()
        return

    cursor.execute('DELETE FROM NhanSu WHERE cccd = ?', (cccd,))
    conn.commit()
    print(f"\n[+] Đã xóa thành công nhân sự có số CCCD: {cccd}")
    conn.close()

def in_danh_sach(danh_sach):
    """Hàm phụ trợ để in danh sách nhân sự theo định dạng bảng."""
    if not danh_sach:
        print("\nKhông có dữ liệu để hiển thị.")
        return
        
    print("-" * 95)
    print(f"{'Số CCCD':<15} | {'Họ và Tên':<25} | {'Ngày Sinh':<12} | {'Giới Tính':<10} | {'Địa Chỉ Thường Trú':<25}")
    print("-" * 95)
    for nv in danh_sach:
        print(f"{nv[0]:<15} | {nv[1]:<25} | {nv[2]:<12} | {nv[3]:<10} | {nv[4]:<25}")
    print("-" * 95)

def hien_thi_danh_sach():
    conn = ket_noi_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM NhanSu')
    data = cursor.fetchall()
    print("\n--- DANH SÁCH TẤT CẢ NHÂN SỰ ---")
    in_danh_sach(data)
    conn.close()

def tim_kiem_nhan_su(tu_khoa):
    conn = ket_noi_db()
    cursor = conn.cursor()
    # Tìm kiếm tương đối bằng toán tử LIKE (tìm theo CCCD, Tên hoặc Địa chỉ)
    tu_khoa_like = f"%{tu_khoa}%"
    cursor.execute('''
        SELECT * FROM NhanSu 
        WHERE cccd LIKE ? OR ho_ten LIKE ? OR dia_chi LIKE ?
    ''', (tu_khoa_like, tu_khoa_like, tu_khoa_like))
    data = cursor.fetchall()
    
    print(f"\n--- KẾT QUẢ TÌM KIẾM CHO: '{tu_khoa}' ---")
    in_danh_sach(data)
    conn.close()

# ==========================================
# GIAO DIỆN CHƯƠNG TRÌNH (MENU)
# ==========================================
def main():
    tao_bang_neu_chua_co()
    
    while True:
        print("\n" + "="*40)
        print("  QUẢN LÝ NHÂN SỰ (LƯU TRỮ DATABASE)  ")
        print("="*40)
        print("1. Thêm mới nhân sự")
        print("2. Sửa thông tin nhân sự")
        print("3. Xóa nhân sự")
        print("4. Xem hiển thị danh sách nhân sự")
        print("5. Tìm kiếm nhân sự (theo CCCD, tên, địa chỉ)")
        print("0. Thoát chương trình")
        print("="*40)
        
        lua_chon = input("Nhập lựa chọn của bạn (0-5): ")
        
        if lua_chon == '1':
            print("\n--- THÊM NHÂN SỰ ---")
            cccd = input("Nhập số CCCD: ")
            ho_ten = input("Nhập Họ và Tên: ")
            ngay_sinh = input("Nhập Ngày sinh (VD: 01/01/1990): ")
            gioi_tinh = input("Nhập Giới tính: ")
            dia_chi = input("Nhập Địa chỉ thường trú: ")
            them_nhan_su(cccd, ho_ten, ngay_sinh, gioi_tinh, dia_chi)
            
        elif lua_chon == '2':
            print("\n--- SỬA THÔNG TIN NHÂN SỰ ---")
            cccd = input("Nhập số CCCD của nhân sự cần sửa: ")
            print("Nhập thông tin mới (nhấn Enter nếu không muốn đổi trường đó - *Lưu ý: Code cơ bản này yêu cầu nhập lại toàn bộ):")
            ho_ten = input("Nhập Họ và Tên mới: ")
            ngay_sinh = input("Nhập Ngày sinh mới: ")
            gioi_tinh = input("Nhập Giới tính mới: ")
            dia_chi = input("Nhập Địa chỉ mới: ")
            sua_nhan_su(cccd, ho_ten, ngay_sinh, gioi_tinh, dia_chi)
            
        elif lua_chon == '3':
            print("\n--- XÓA NHÂN SỰ ---")
            cccd = input("Nhập số CCCD của nhân sự cần xóa: ")
            xoa_nhan_su(cccd)
            
        elif lua_chon == '4':
            hien_thi_danh_sach()
            
        elif lua_chon == '5':
            print("\n--- TÌM KIẾM NHÂN SỰ ---")
            tu_khoa = input("Nhập từ khóa (Số CCCD, Tên một phần, hoặc Địa chỉ): ")
            tim_kiem_nhan_su(tu_khoa)
            
        elif lua_chon == '0':
            print("Đã thoát chương trình. Tạm biệt!")
            break
        else:
            print("[!] Lựa chọn không hợp lệ, vui lòng nhập lại.")

if __name__ == "__main__":
    main()