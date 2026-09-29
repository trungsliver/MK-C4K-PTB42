# Danh sách: Array / List
    # là 1 cấu trúc dữ liệu
    # Các thao tác cơ bản: CRUD (Create - Read - Update - Delete)

# Create - Khởi tạo danh sách
    # Danh sách rỗng (không có phần tử)
arr = []
    # Danh sách có phần tử
ptb42 = ['Khương', 'Phong', 'Cường', 'Bình', 'Khôi']
arr1 = ['Đăng', 14, 8.5, True]

# Read - Duyệt phần tử
    # len() - độ dài / số lượng phần tử 
print('Số lượng phần tử arr:', len(arr))
print('Số lượng phần tử ptb42:', len(ptb42))

    # Hiện phần tử bằng chỉ số index
print('Phần tử đầu tiên:', ptb42[0])
print('Phần tử có index=2:', ptb42[2])
print('Phần tử cuối cùng:', ptb42[-1])

    #  Duyệt danh sách
        # Cách 1: Dùng cả index và value
for i in range(len(ptb42)):
    print(f'Index = {i}. Value = {ptb42[i]}')
        # Cách 2: Chỉ dùng value
for item in ptb42:
    print('Value:', item)
        # Cách 3: Dùng hàm có sẵn
for index, value in enumerate(ptb42):
    print(f'Index = {index}. Value = {value}')

    # Hiển thị toàn bộ phần tử danh sách
print(ptb42)

# Update - Cập nhật 
    # Thêm phần tử vào cuối danh sách - append(value)
ptb42.append('Nam')
    # Thêm phần tử vào vị trí chỉ định - insert(index, value)
ptb42.insert(2, 'Imposter')
    # Sửa phần tử cũ
ptb42[2] = 'Trung'

# Delete - Xóa phần tử 
    # Xóa bằng giá trị - remove(value)
ptb42.remove('Nam')
    # Xóa bằng chỉ số index - pop(index)
ptb42.pop(2)
    # Xóa toàn bộ phần tử danh sách
ptb42.clear()

# Sắp xếp phần tử - sort()
num_list = [5, 2, 9, 7, 1, 6, 3, 8, 4]
    # Theo thứ tự tăng dần
num_list.sort()
    # Theo thứ tự giảm dần
num_list.sort(reverse=True)
print(num_list)

# Tìm giá trị phần tử lớn nhất / nhỏ nhất
print('Phần tử lớn nhất:', max(num_list))
print('Phần tử nhỏ nhất:', min(num_list))

# ============== LUYỆN TẬP =================
# Bài 1: Nhập từ bàn phím 1 số nguyên n
# Yêu cầu: Kiểm tra xem n có phải là số nguyên tố hay không
# Biết rằng số nguyên tố là số chỉ chia hết cho 1 và chính nó

n = int(input('Nhập số nguyên n: '))
    # Khai báo biến count để đểm số lượng ước số của n
count = 0

    # Duyệt i trong khoảng [1, n]
for i in range(1, n+1):
    # Nếu n chia hết cho i thì tăng count lên 1
    if n % i == 0:
        count += 1

    # Hiển thị kết quả
if count == 2:
    print(n, 'là số nguyên tố')
else:
    print(n, 'không phải số nguyên tố')

# Bài 2: In ra các số nguyên tố trong khoảng [50,100] và tính tổng các số đó
    # Khai báo biến lưu tổng các số nguyên tố
total = 0
    # Duyệt n trong khoảng [50, 100]
for n in range(50, 101):
    # Khai báo biến count để đểm số lượng ước số của n
    count = 0
    # Duyệt i trong khoảng [1, n]
    for i in range(1, n+1):
        # Nếu n chia hết cho i thì tăng count lên 1
        if n % i == 0:
            count += 1
    # Hiển thị kết quả & cộng vào biến total
    if count == 2:
        total += n
        print(n, end = ' ')
print(f'\nTổng các số nguyên tố trong khoảng [50,100] là: {total}')