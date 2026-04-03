
# 1. Viết hàm tính tổng 2 số truyền vào
def tinh_tong_2_so(a, b):
    return a + b

# 2. Viết hàm tính tổng các số truyền vào
def tinh_tong_cac_so(*args):
    tong = 0
    for so in args:
        tong += so
    return tong

# 3. Viết hàm kiểm tra một số nguyên tố0
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 4. Viết chương trình tìm các số nguyên tố trong khoảng [a, b]
def tim_so_nguyen_to(a, b):
    ds = []
    for i in range(a, b + 1):
        if la_so_nguyen_to(i):
            ds.append(i)
    return ds

# 5. Viết hàm kiểm tra số hoàn hảo
def la_so_hoan_hao(n):
    if n < 2:
        return False
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc == n

# 6. Viết chương trình tìm các số hoàn hảo trong khoảng [a, b]
def tim_so_hoan_hao(a, b):
    ds = []
    for i in range(a, b + 1):
        if la_so_hoan_hao(i):
            ds.append(i)
    return ds

# 7. Viết chương trình menu chọn thực thi các hàm ở trên
def menu():
    while True:
        print("\n" + "=" * 40)
        print("         MENU CHƯƠNG TRÌNH")
        print("=" * 40)
        print("1. Tính tổng 2 số")
        print("2. Tính tổng các số")
        print("3. Kiểm tra số nguyên tố")
        print("4. Tìm số nguyên tố trong khoảng [a, b]")
        print("5. Kiểm tra số hoàn hảo")
        print("6. Tìm số hoàn hảo trong khoảng [a, b]")
        print("0. Thoát")
        print("=" * 40)

        lua_chon = input("Nhập lựa chọn của bạn: ")

        if lua_chon == "1":
            a = float(input("Nhập số thứ nhất: "))
            b = float(input("Nhập số thứ hai: "))
            print(f"Tổng của {a} và {b} là: {tinh_tong_2_so(a, b)}")

        elif lua_chon == "2":
            n = int(input("Nhập số lượng các số: "))
            cac_so = []
            for i in range(n):
                so = float(input(f"Nhập số thứ {i + 1}: "))
                cac_so.append(so)
            print(f"Tổng các số là: {tinh_tong_cac_so(*cac_so)}")

        elif lua_chon == "3":
            n = int(input("Nhập một số nguyên: "))
            if la_so_nguyen_to(n):
                print(f"{n} là số nguyên tố")
            else:
                print(f"{n} không phải là số nguyên tố")

        elif lua_chon == "4":
            a = int(input("Nhập a: "))
            b = int(input("Nhập b: "))
            ds = tim_so_nguyen_to(a, b)
            if ds:
                print(f"Các số nguyên tố trong [{a}, {b}]: {ds}")
            else:
                print(f"Không có số nguyên tố trong [{a}, {b}]")

        elif lua_chon == "5":
            n = int(input("Nhập một số nguyên: "))
            if la_so_hoan_hao(n):
                print(f"{n} là số hoàn hảo")
            else:
                print(f"{n} không phải là số hoàn hảo")

        elif lua_chon == "6":
            a = int(input("Nhập a: "))
            b = int(input("Nhập b: "))
            ds = tim_so_hoan_hao(a, b)
            if ds:
                print(f"Các số hoàn hảo trong [{a}, {b}]: {ds}")
            else:
                print(f"Không có số hoàn hảo trong [{a}, {b}]")

        elif lua_chon == "0":
            print("Tạm biệt!")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại!")

# Chạy chương trình
if __name__ == "__main__":
    menu()
