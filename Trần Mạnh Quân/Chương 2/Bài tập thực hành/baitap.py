import os

# Lấy đường dẫn thư mục chứa file source code
thu_muc = os.path.dirname(os.path.abspath(__file__))


def bai1():
    """B1: Đọc n dòng đầu tiên của một tập tin"""
    print("=" * 50)
    print("BÀI 1: Đọc n dòng đầu tiên của tập tin")
    print("=" * 50)

    ten_file = input("Nhập tên tập tin cần đọc: ")
    duong_dan = os.path.join(thu_muc, ten_file)

    if not os.path.exists(duong_dan):
        print(f"Tập tin '{ten_file}' không tồn tại!")
        return

    try:
        n = int(input("Nhập số dòng cần đọc (n): "))
    except ValueError:
        print("Vui lòng nhập một số nguyên!")
        return

    with open(duong_dan, "r", encoding="utf-8") as f:
        print(f"\n--- {n} dòng đầu tiên của '{ten_file}' ---")
        for i, dong in enumerate(f):
            if i >= n:
                break
            print(dong, end="")
    print()


def bai2():
    """B2: Ghi đoạn văn bản vào tập tin và hiển thị"""
    print("=" * 50)
    print("BÀI 2: Ghi văn bản vào tập tin và hiển thị")
    print("=" * 50)

    ten_file = input("Nhập tên tập tin cần ghi: ")
    duong_dan = os.path.join(thu_muc, ten_file)

    print("Nhập nội dung văn bản (nhập dòng trống để kết thúc):")
    noi_dung = []
    while True:
        dong = input()
        if dong == "":
            break
        noi_dung.append(dong)

    van_ban = "\n".join(noi_dung)

    with open(duong_dan, "w", encoding="utf-8") as f:
        f.write(van_ban)

    print(f"\nĐã ghi vào tập tin '{ten_file}' thành công!")
    print(f"\n--- Nội dung tập tin '{ten_file}' ---")
    with open(duong_dan, "r", encoding="utf-8") as f:
        print(f.read())


def bai3():
    """B3: Tạo file demo_file1.txt và đọc nội dung"""
    print("=" * 50)
    print("BÀI 3: Tạo và đọc file demo_file1.txt")
    print("=" * 50)

    ten_file = "demo_file1.txt"
    duong_dan = os.path.join(thu_muc, ten_file)
    noi_dung = "Thuc \n hanh \n voi \n file\n IO\n"

    # Tạo file với nội dung cho trước
    with open(duong_dan, "w", encoding="utf-8") as f:
        f.write(noi_dung)
    print(f"Đã tạo file '{ten_file}' thành công!")

    # a) In nội dung file trên một dòng
    print("\na) Nội dung file trên một dòng:")
    with open(duong_dan, "r", encoding="utf-8") as f:
        noi_dung_doc = f.read()
        print(noi_dung_doc.replace("\n", " "))

    # b) In nội dung file theo từng dòng
    print("b) Nội dung file theo từng dòng:")
    with open(duong_dan, "r", encoding="utf-8") as f:
        for dong in f:
            print(dong, end="")
    print()


def menu():
    while True:
        print("\n" + "=" * 50)
        print("     BÀI TẬP THỰC HÀNH - CHƯƠNG 2")
        print("=" * 50)
        print("1. Bài 1: Đọc n dòng đầu tiên của tập tin")
        print("2. Bài 2: Ghi văn bản vào tập tin và hiển thị")
        print("3. Bài 3: Tạo và đọc file demo_file1.txt")
        print("0. Thoát")
        print("=" * 50)

        lua_chon = input("Chọn bài tập (0-3): ")

        if lua_chon == "1":
            bai1()
        elif lua_chon == "2":
            bai2()
        elif lua_chon == "3":
            bai3()
        elif lua_chon == "0":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng chọn lại.")


if __name__ == "__main__":
    menu()
