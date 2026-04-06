# Bảng mã hóa mặc định theo đề bài (có thể mở rộng thêm)
ENCODE_DICT = {
    'a': '!', 'b': '@', 'c': '#', 'd': '$',
    'e': '%', 'f': '^', 'g': '&', 'h': '*',
    'i': '(', 'j': ')', 'k': '-', 'l': '_',
    'm': '=', 'n': '+', 'o': '[', 'p': ']',
    'q': '{', 'r': '}', 's': ';', 't': ':',
    'u': "'", 'v': '"', 'w': ',', 'x': '<',
    'y': '.', 'z': '>', ' ': '~'
}

# Tạo bảng giải mã tự động bằng cách đảo ngược key - value từ bảng mã hóa
DECODE_DICT = {value: key for key, value in ENCODE_DICT.items()}


def ma_hoa(van_ban):
    """Hàm mã hóa văn bản"""
    van_ban_da_ma_hoa = ""
    for ky_tu in van_ban:
        # Chuyển về chữ thường để mã hóa (nếu muốn hỗ trợ chữ hoa thì phải thêm vào Dictionary)
        ky_tu_thuong = ky_tu.lower()
        if ky_tu_thuong in ENCODE_DICT:
            van_ban_da_ma_hoa += ENCODE_DICT[ky_tu_thuong]
        else:
            # Nếu ký tự không có trong bảng mã (ví dụ: số), giữ nguyên
            van_ban_da_ma_hoa += ky_tu
    return van_ban_da_ma_hoa


def giai_ma(van_ban):
    """Hàm giải mã văn bản"""
    van_ban_da_giai_ma = ""
    for ky_tu in van_ban:
        if ky_tu in DECODE_DICT:
            van_ban_da_giai_ma += DECODE_DICT[ky_tu]
        else:
            # Nếu ký tự không có trong bảng giải mã, giữ nguyên
            van_ban_da_giai_ma += ky_tu
    return van_ban_da_giai_ma


def main():
    while True:
        print("\n" + "="*40)
        print("  CHƯƠNG TRÌNH MÃ HÓA / GIẢI MÃ")
        print("="*40)
        print("1. Mã hóa văn bản")
        print("2. Giải mã văn bản")
        print("0. Thoát")
        
        luachoan = input("Vui lòng chọn chức năng (0-2): ").strip()
        
        if luachoan == '1':
            van_ban = input("Nhập văn bản cần mã hóa: ")
            ket_qua = ma_hoa(van_ban)
            print(f"[*] Kết quả mã hóa: {ket_qua}")
            
        elif luachoan == '2':
            van_ban = input("Nhập mã cần giải: ")
            ket_qua = giai_ma(van_ban)
            print(f"[*] Kết quả giải mã: {ket_qua}")
            
        elif luachoan == '0':
            print("Đã thoát chương trình.")
            break
            
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại!")


if __name__ == "__main__":
    main()
