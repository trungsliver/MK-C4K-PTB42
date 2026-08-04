# phím tắt ghi chú - comment: ctrl /

# Hiện dữ liệu ra màn hình
print("Hello World")

# Biến số - Variables
    # Tác dụng: Lưu trữ dữ liệu
    # Đặc điểm: có thể thay đổi được khi lập trình
name = 'Duc Trung'
a, b, c = 1, 2, 3

print(name)

# Quy tắc đặt tên biến:
    # Chỉ gồm chữ cái tiếng anh, số, dấu gạch dưới
    # Không được bắt đầu bằng số
    # Không trùng với các từ khóa (tên câu lệnh) của Python

# 2 kiểu đặt tên phổ biến:
    # camelCase (lạc đà): viết hoa chữ cái đầu mỗi từ, trừ từ đầu tiên
myName = 'Duc Trung'
    # snake_case (rắn): có dấu gạch dưới giữa các từ 
my_name = 'Duc Trung'

# Nhập dữ liệu - input()
game = input('Hãy nhập game bạn thích: ')
print(game)

food = input('Nhập đồ ăn bạn thích: ')
print(food)

# Các cách hiển thị dữ liệu (4 cách)
name = 'Duc Trung'
age = 2
school = 'MindX'
    # cách 1: Dùng dấu cộng +
print('Họ tên: ' + name)
    # cách 2: Dùng dấu phẩy ,
print('Tuổi:', age)
    # cách 3: Dùng f-string (truyền dữ liệu vào string)
print(f'Tôi tên là {name}, tôi {age} tuổi, tôi học ở trường {school}')
    # cách 4: Hiển thị trên nhiều dòng
print(f'''
========== THÔNG TIN ==========
Họ tên: {name}
Tuổi: {age}
Trường: {school}
===============================''')