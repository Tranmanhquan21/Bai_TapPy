def bai_1():
    print("\n" + "-" * 40)
    print("BÀI 1: Thêm phần tử 'c' vào vị trí số 2 của tuple")
    print("-" * 40)
    _tuple = ('a', 'b', 'd', 'e')
    print(f"Tuple ban đầu: {_tuple}")
    
    # Vì tuple là kiểu dữ liệu không thể thay đổi (immutable),
    # ta có thể chuyển sang list để dùng hàm insert, sau đó chuyển lại thành tuple
    temp_list = list(_tuple)
    temp_list.insert(2, 'c')
    _new_tuple = tuple(temp_list)
    
    # Hoặc có thể dùng slicing: _new_tuple = _tuple[:2] + ('c',) + _tuple[2:]
    
    print(f"Tuple mới    : {_new_tuple}")


def bai_2():
    print("\n" + "-" * 40)
    print("BÀI 2: Loại bỏ các phần tử có giá trị giống nhau (chỉ giữ phần tử xuất hiện 1 lần)")
    print("-" * 40)
    _tuple = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab')
    print(f"Tuple ban đầu: {_tuple}")
    
    # Dùng hàm tuple() kết hợp với generator expression và hàm count
    # Chỉ lấy những phần tử có số lần đếm (_tuple.count(x)) đúng bằng 1
    _new_tuple = tuple(x for x in _tuple if _tuple.count(x) == 1)
    
    print(f"Tuple mới    : {_new_tuple}")


def bai_3():
    print("\n" + "-" * 40)
    print("BÀI 3: Loại bỏ trùng lặp trong tuple (mỗi giá trị giữ lại 1 lần)")
    print("-" * 40)
    _tuple = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab')
    print(f"Tuple ban đầu: {_tuple}")
    
    temp_list = []
    for ky_tu in _tuple:
        # Nếu phần tử chưa xuất hiện trong danh sách tạm thì thêm vào
        if temp_list.count(ky_tu) == 0:
            temp_list.append(ky_tu)
            
    _new_tuple = tuple(temp_list)
    print(f"Tuple mới    : {_new_tuple}")


def main():
    while True:
        print("\n" + "=" * 50)
        print("               MENU CHỌN BÀI TẬP TUPLE")
        print("=" * 50)
        print("1. Bài 1: Thêm phần tử 'c' vào tuple")
        print("2. Bài 2: Loại bỏ phần tử xuất hiện nhiều lần (chỉ giữ phần tử duy nhất)")
        print("3. Bài 3: Loại bỏ trùng lặp (lấy giá trị đại diện)")
        print("0. Thoát")
        print("=" * 50)
        
        choice = input("Vui lòng nhập lựa chọn của bạn (0-3): ").strip()
        
        if choice == '1':
            bai_1()
        elif choice == '2':
            bai_2()
        elif choice == '3':
            bai_3()
        elif choice == '0':
            print("\nĐã thoát chương trình. Tạm biệt!\n")
            break
        else:
            print("\nLựa chọn không hợp lệ, vui lòng chọn lại!")


if __name__ == "__main__":
    main()
