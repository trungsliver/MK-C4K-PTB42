# ========================== Ôn tập ==========================
# Bài 1: Nhập vào từ bàn phím các thông tin các nhân: 
    # Họ tên, Tuổi, Trường học, giới tính, điểm trung bình.
    # In ra màn hình các thông tin vừa nhập
name = input('Nhập tên: ')
age = int(input('Nhập tuổi: '))
school = input('Nhập trường học: ')
gender = input('Nhập giới tính: ')
score = float(input('Nhập điểm trung bình: '))

print('===== Thông tin cá nhân =====')
print('Họ tên:', name)
print('Tuổi:', age)
print('Trường học:', school)
print('Giới tính:', gender)
print('Điểm trung bình:', score)

# Bài 2: Nhập vào chiều dài và chiều rộng hình chữ nhật
    # In ra màn hình chu vi và diện tích hình chữ nhật đó.
length = float(input('Nhập chiều dài: '))
width = float(input('Nhập chiều rộng: '))

perimeter = 2 * (length + width)
area = length * width

print('===== Hình chữ nhật =====')
print('Chu vi:', perimeter)
print('Diện tích:', area)

# Bài 3: Nhập số nguyên n từ bàn phím.
    # Kiểm tra xem n có phải là số chẵn hay không.
number = int(input('Nhập số nguyên n: '))
if number % 2 == 0:
    print(number, "là số chẵn")
else:
    print(number, "là số lẻ")

# Bài 4: Nhập điểm số từ bàn phím. Hãy in ra mà hình xếp hạng học lực, biết rằng:
    # 8-10: Giỏi, 6.5-8: Khá, 5-6.5: Trung Bình, 0-5: Yếu
score = float(input('Hãy nhập điểm của bạn: '))
if 8 <= score <= 10:
    print('Xếp loại: Giỏi')
elif 6.5 <= score < 8:
    print('Xếp loại: Khá')
elif 5 <= score < 6.5:
    print('Xếp loại: Trung bình')
elif 0 <= score < 5:
    print('Xếp loại: Yếu')
else:
    print('Điểm không hợp lệ')

# Bài 5: Nhập 2 số nguyên a và b từ bàn phím
a = int(input('Nhập a: '))
b = int(input('Nhập b: '))
    # Yêu cầu 1: In ra tất cả các số trong khoảng [a, b] hoặc ngược lại
if a > b:
    a, b = b, a
print(f'Các số trong khoảng [{a}, {b}]: ')
for i in range(a, b+1):
    print(i, end=' ')

    # Yêu cầu 2: Tính tổng các số chia hết cho 3 trog khoảng vừa in
total = 0
for i in range(a, b+1):
    if i % 3 == 0:
        total += i
print(f'\nTổng các số chia hết cho 3 trong khoảng [{a}, {b}] là: {total}')

    # Yêu cầu 3: In ra số lượng số lẻ có trong khoảng trên
count = 0
for i in range(a, b+1):
    if i % 2 != 0:
        count += 1
print(f'Số lượng số lẻ trong khoảng [{a}, {b}] là: {count}')

# Bài 6: In ra bảng cửu chương từ 5 đến 9

# Bài 7: Nhập số nguyên dương n. Tính tổng tất cả các chữ số của n.
    # Ví dụ: n = 123 => Tổng các chữ số = 1+2+3 = 6

# Bài 8: Nhập n là số giây cần chuyển đổi (số nguyên)
    # In ra màn hình dạng h-m-s
    # Ví dụ: 3661s = 1h 1p 1s

# Bài 9: Danh sách
    # YC1: Nhập vào từ bàn phím 1 danh sách bao gồm 10 số nguyên
    # YC2: Thêm số '-5' vào vị trí thứ 2 (index=2) trong danh sách
    # YC3: Tính tổng các cố chẵn trong danh sách
    # YC4: Đếm số lượng số lẻ có trong danh sách
    # YC5: Tìm giá trị phần tử lớn nhất của danh sách
    # YC6: Tìm vị trí phần tử nhỏ nhất của danh sách
    # YC7: Dùng hàm tính giá trị trung bình của các phần tử trong danh sách

# Bài 10: Nhập vào từ bàn phím 1 chuỗi ký tự bao gồm các số nguyên, các số này cách nhau 1 khoảng trắng (hoặc dấu ,).
    # Yêu cầu 1: Tách chuỗi và thêm vào danh sách có tên num_list
    # Yêu cầu 2: Chuyển đổi toàn bộ phần tử trong danh sách num_list thành kiểu dữ liệu int.
    # Yêu cầu 3: In ra màn hình số lượng số lẻ của num_list.

# Bài 11: Dùng thư viên random để thêm ngẫu nhiên các số nguyên trong khoảng [20,50] vào 2 danh sách arr1 và arr2.
    # Yêu cầu 1: Hãy viết hàm/chương trình con in ra phần tử chung của 2 danh sách vừa tạo
    # Yêu cầu 2: In ra màn hình vị trí phần tử nhỏ nhất của danh sách arr1
    # Yêu cầu 3: In ra màn hình vị trí phần tử lớn nhất của danh sách arr2

# Bài 12: Hãy nhập từ bàn phím họ tên của bạn.
    # Yêu cầu 1: Chuyển đổi chuỗi ký tự tên thành chuỗi ký tự viết hoa
    # Yêu cầu 2: Chuyển đổi chuỗi ký tự tên thành chuỗi ký tự viết thường
    # Yêu cầu 3: Chuyển đổi chuỗi ký tự tên thành chuỗi ký tự viết hoa các chữ cái đầu