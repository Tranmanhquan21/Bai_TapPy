a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))

# a) Tổng và tích
print("Tổng =", a + b + c)
print("Tích =", a * b * c)

# b) Hiệu (ví dụ a - b)
print("Hiệu a - b =", a - b)

# c) Chia (ví dụ a chia b)
if b != 0:
    print("Phần nguyên =", a // b)
    print("Phần dư =", a % b)
    print("Chia chính xác =", a / b)
else:
    print("Không thể chia cho 0")