n = int(input("Nhập số nguyên dương: "))

if n % 2 == 0 and n % 3 == 0:
    print("Chia hết cho cả 2 và 3")
elif n % 2 == 0:
    print("Chia hết cho 2")
elif n % 3 == 0:
    print("Chia hết cho 3")
else:
    print("Không chia hết cho 2 và 3")