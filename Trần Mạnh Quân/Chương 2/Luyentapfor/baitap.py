class BaiTap:


    def bai1(self):
        n = int(input("Nhập số nguyên n: "))
        print("Kết quả:")

        for i in range(1, n):
            print(f"{2*i} = 2*{i}")

   
    def bai2(self):
        n = int(input("Nhập số nguyên n: "))

        if n > 10:
            print("Số nhập vào phải bé hơn 10.")
        else:
            print("Các số chẵn từ 1 đến", n, "là:")
            for i in range(2, n + 1, 2):
                print(i)

    
    def bai3(self):
        print("Các số từ 80 đến 100 chia hết cho 2 và 3 là:")
        for i in range(80, 101):
            if i % 2 == 0 and i % 3 == 0:
                print(i)

    
    def bai4(self):
        n = int(input("Nhập số nguyên n (<20): "))

        if n >= 20:
            print("Vui lòng nhập số nhỏ hơn 20.")
        else:
            print("Các số từ 1 đến", n, "chia hết cho 5 hoặc 7 là:")
            for i in range(1, n + 1):
                if i % 5 == 0 or i % 7 == 0:
                    print(i)



def menu():
    bt = BaiTap()

    while True:
        print("\n========= MENU =========")
        print("1. Bài 1")
        print("2. Bài 2")
        print("3. Bài 3")
        print("4. Bài 4")
        print("0. Thoát")
        print("========================")

        choice = input("Chọn bài: ")

        if choice == "1":
            bt.bai1()
        elif choice == "2":
            bt.bai2()
        elif choice == "3":
            bt.bai3()
        elif choice == "4":
            bt.bai4()
        elif choice == "0":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ!")

