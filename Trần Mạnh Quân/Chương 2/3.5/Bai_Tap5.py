import math

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

# Trường hợp a = 0 → phương trình bậc 1
if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        x = -c / b
        print("Nghiệm x =", x)
else:
    delta = b**2 - 4*a*c

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("2 nghiệm phân biệt:", x1, x2)
    elif delta == 0:
        x = -b / (2*a)
        print("Nghiệm kép:", x)
    else:
        print("Phương trình vô nghiệm")