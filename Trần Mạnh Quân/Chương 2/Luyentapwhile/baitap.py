class LuyenTapWhile:

   
    def bai1(self):
        i = 1
        tich = 1

        while i <= 10:
            tich *= i
            i += 1

        print("Tích của 10 số tự nhiên đầu tiên là:", tich)


    def bai2(self):
        n = int(input("Nhập số nguyên dương n: "))
        i = 1
        giai_thua = 1

        while i <= n:
            giai_thua *= i
            i += 1

        print(f"{n}! =", giai_thua)

    def bai3(self):
        n = int(input("Nhập số nguyên dương n: "))

        if n < 2:
            print("Không phải số nguyên tố.")
            return

        i = 2
        la_so_nguyen_to = True

        while i <= n // 2:
            if n % i == 0:
                la_so_nguyen_to = False
                break
            i += 1

        if la_so_nguyen_to:
            print("Đây là số nguyên tố.")
        else:
            print("Không phải số nguyên tố.")


    def bai4(self):
        n = int(input("Nhập số nguyên n: "))
        i = 1
        tong = 0

        while i < n:
            if i % 2 == 0:
                tong += i
            i += 1

        print("Tổng các số chẵn nhỏ hơn", n, "là:", tong)


# ===== MENU =====
def menu():
    bt = LuyenTapWhile()

    while True:
        print("\n======= MENU =======")
        print("1. Bài 1")
        print("2. Bài 2")
        print("3. Bài 3")
        print("4. Bài 4")
        print("0. Thoát")
        print("====================")

        chon = input("Chọn bài: ")

        if chon == "1":
            bt.bai1()
        elif chon == "2":
            bt.bai2()
        elif chon == "3":
            bt.bai3()
        elif chon == "4":
            bt.bai4()
        elif chon == "0":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ!")


# ===== CHẠY CHƯƠNG TRÌNH =====
menu()