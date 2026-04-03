# B4: Nhập từ bàn phím và lưu/đọc file setInfo.txt

def b4_write_info(filename='setInfo.txt'):
    print('--- B4a: Nhập thông tin cá nhân ---')
    info = {}
    info['ten'] = input('Tên: ').strip()
    info['tuoi'] = input('Tuổi: ').strip()
    info['email'] = input('Email: ').strip()
    info['skype'] = input('Skype: ').strip()
    info['diachi'] = input('Địa chỉ: ').strip()
    info['noilamviec'] = input('Nơi làm việc: ').strip()

    with open(filename, 'w', encoding='utf-8') as f:
        for k, v in info.items():
            f.write(f'{k}:{v}\n')

    print(f'Dã lưu thông tin vào "{filename}".')


def b4_read_info(filename='setInfo.txt'):
    print(f'--- B4b: Đọc lại thông tin từ "{filename}" ---')
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f'File "{filename}" không tồn tại. Vui lòng chạy chức năng lưu trước.')
        return

    info = {}
    for line in lines:
        if ':' in line:
            key, value = line.split(':', 1)
            info[key.strip()] = value.strip()

    if not info:
        print('Không có dữ liệu hợp lệ trong file.')
        return

    print('Thông tin cá nhân:')
    for k, v in info.items():
        print(f'  {k}: {v}')


# B5: Đếm số lượng xuất hiện của từ trong file demo_file2.txt

def b5_count_words(filename='demo_file2.txt'):
    text = 'Dem so luong tu xuat hien abc abc abc 12 12 it it eaut'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read().strip()

    # Chuyển về dạng tách từ (split theo khoan trắng) và chuẩn hóa không phân biệt hoa/thường
    tokens = [w.strip() for w in content.split() if w.strip()]

    counts = {}
    for token in tokens:
        counts[token] = counts.get(token, 0) + 1

    print(f'File "{filename}" nội dung:')
    print(content)
    print('Số lượng xuất hiện từng từ:')
    print(counts)
    return counts


if __name__ == '__main__':
    # Chạy lần lượt B4 và B5
    b4_write_info('setInfo.txt')
    print('')
    b4_read_info('setInfo.txt')
    print('\n--- Chạy B5 ---')
    b5_count_words('demo_file2.txt')
