# Variables - Biến số
    # Tác dụng: Dùng để lưu trữ dữ liệu
    # Đặc điểm: có thể thay đổi được khi lập trình
name = 'Duc Trung'
a, b, c = 1, 2, 3

# Quy tắc đặt tên biến:
    # Chỉ gồm chữ tiếng anh, số, dấu gạch dưới _
    # Không được bắt đầu bằng số
    # Không trùng với các từ khóa (tên câu lệnh) của Python

# 2 kiểu đặt tên biến:
    # camelCase (lạc đà): viết hoa chữ cái đầu mỗi từ, trừ từ đầu tiên
myNameInSchool = 'Duc Trung'
    # snake_case (rắn): có dấu gạch dưới giữa các từ 
my_name_in_school = 'Duc Trung'

# Data Types - Kiểu dữ liệu
    # String: chuỗi / xâu ký tự
name = 'Duc Trung'
school = "MindX Technology School"
    # int (integer): số nguyên
age = 2
    # float: số thực
height = 1.7
    # bool / boolean: đúng hoặc sai (True / False)
is_male = True

# Kiểm tra kiểu dữ liệu: type()
print('Kiểu dữ liệu của name:', type(name))
print('Kiểu dữ liệu của age:', type(age))
print('Kiểu dữ liệu của height:', type(height))
print('Kiểu dữ liệu của is_male:', type(is_male))

# Nhập dữ liệu - input()
# score = input('Nhập điểm của bạn: ')
# print('Kiểu dữ liệu của score:', type(score))

# weight = float(input('Nhập cân nặng của bạn: '))
# print('Kiểu dữ liệu của weight:', type(weight))

# number_of_siblings = int(input('Nhập số anh chị em của bạn: '))
# print('Kiểu dữ liệu của number_of_siblings:', type(number_of_siblings))

# Chuyển đổi kiểu dữ liệu:
a = "123"
print('Kiểu dữ liệu của a:', type(a))
b = float(a)
print('Kiểu dữ liệu của b:', type(b))


# Toán tử số học:
    # Cơ bản: + - * /
print('7 / 2 =', 7 / 2)
    # Chia lấy nguyên: //
print('7 // 2 =', 7 // 2)
    # Chia lấy dư: %
print('7 % 2 =', 7 % 2)
    # Lũy thừa: ** 
print('2^2^3 =', 2**2**3)

# Lưu ý:
    # Thứ tự thực hiện phép tính: Lũy thừa -> Nhân chia -> Cộng trừ
    # Nếu có nhiều lũy thừa thì thực hiện từ phải sang trái

#  ======================= LUYỆN TẬP =======================
#  Bài 1: Chuyển đổi USD sang VND
    # Nhập số USD cần chuyển đổi (float)
usd = float(input('Nhập số USD cần chuyển đổi sang VND: $'))
    # Đổi USD sang VND (1 USD = 26 000 VND)
vnd = usd * 26000
    # Hiển thị kết quả (VD: 1 USD = 26 000 VND)
print(f'${usd} = {vnd} VND')

# Bài 2: Nhập chiều dài, chiều rộng HCN và tính diện tích, chu vi
    # Nhập chiều dài, chiều rộng HCN (float)
length = float(input('Nhập chiều dài HCN: '))
width = float(input('Nhập chiều rộng HCN: '))
    # Tính chu vi, diện tích HCN
cvi = (length + width) * 2
s = length * width
    # Hiển thị kết quả
print('Chu vi HCN =', cvi)
print('Diện tích HCN =', s)
