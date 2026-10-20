# ============ Hàm / Chương trình con ============
    # Khái niệm: 1 nhóm các câu lệnh nhằm thực hiện 1 nhiệm vụ cụ thể
    # Đặc điểm: có thể tái sử dụng (sử dụng được nhiều lần)

# Cấu trúc cơ bản
def introduce():
    print('Xin chào, tôi tên là Cường!')
    print('Tôi 12 tuổi.')
    print('Tôi sống ở Hà Nội.')

# Gọi hàm
introduce()
introduce()

# Parameter (tham số đầu vào)
def introduce(name, age, address):
    print('Xin chào, tôi tên là', name)
    print('Tôi', age, 'tuổi.')
    print('Tôi sống ở', address)

# Gọi hàm với tham số
introduce('Bình', 13, 'Hà Nội')
introduce('Phong', 13, 'Hà Nội')

# return (giá trị trả về)
    # Lưu ý: 
        # - Hàm có return sẽ sử dụng như 1 giá trị (biến)
        # - Khi gặp return, hàm sẽ dừng lại

def is_even_number(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Gọi hàm
print('10 là số chẵn:', is_even_number(10))      # True
print('11 là số chẵn:', is_even_number(11))      # False

# ============= Ví Dụ ==============
    # Tính diện tích HCN
def calculate_area_rectangle(length, width):
    area = length * width
    return area

print('Diện tích HCN:', calculate_area_rectangle(5, 10))      # 50

    # Tính chu vi HCN
def calculate_perimeter_rectangle(length, width):
    perimeter = (length + width) * 2
    return perimeter

print('Chu vi HCN:', calculate_perimeter_rectangle(5, 10))      # 30

# ================== LUYỆN TẬP =======================
# Bài 1: Viết một hàm sum_odd(numbers) để tính tổng các số lẻ trong một danh sách numbers.
# 	YC1: Hàm nhận vào một danh sách các số nguyên.
# 	YC2: Hàm trả về tổng các số lẻ trong danh sách đó.
def sum_odd(numbers):
    total_odd = 0                   # Khai báo biến lưu tổng các số lẻ
    for item in numbers:            # Duyệt danh sách theo cách 2 
        if item % 2 != 0:           # Kiểm tra xem số đó có phải là số lẻ không
            total_odd += item       # Cộng số lẻ vào biến lưu tổng
    return total_odd                # Trả về giá trị tổng các số lẻ

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Tổng các số lẻ trong arr:', sum_odd(arr))      

# Bài 2: Viết một hàm is_prime(n) để kiểm tra xem một số nguyên dương n có phải là số nguyên tố hay không.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	YC2: Hàm trả về True nếu n là số nguyên tố, ngược lại trả về False.
def is_prime(n):
    count = 0                    # Biến đếm số lượng ước số của n
    for i in range(1, n + 1):   # Duyệt từ 1 đến n
        if n % i == 0:          # Kiểm tra xem i có phải là ước số của n không
            count += 1          # Nếu có thì tăng biến đếm lên 1
    if count == 2:              # Nếu n có đúng 2 ước số (1 và chính nó) thì n là số nguyên tố
        return True
    else:
        return False

print('7 là số nguyên tố:', is_prime(7))      # True
print('10 là số nguyên tố:', is_prime(10))    # False

# Bài 3: Viết một hàm count_words(s) để đếm số lượng từ trong một chuỗi s.
# 	YC1: Hàm nhận vào một chuỗi ký tự s.
# 	YC2: Hàm trả về số lượng từ trong chuỗi đó.
def count_words(s):
    # strip(): xóa khoảng trắng ở đầu và cuối chuỗi
    # split(): tách chuỗi thành danh sách các từ
    words = s.strip().split()
    return len(words)            # Trả về độ dài của danh sách từ

str1 = 'Xin chào tôi tên là Khương'
print('Số lượng từ trong str1:', count_words(str1))      

# Bài 4: Viết một hàm sum_of_digits(n) để tính tổng các chữ số của một số nguyên dương n.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	YC2: Hàm trả về tổng các chữ số của n.
def sum_of_digits(n:int):
    total = 0
    while n > 0:                    # Duyệt số n cho đến khi n = 0
        total = total + n%10        # Lấy hàng đơn vị của n
        n = n // 10                 # Loại bỏ hàng đơn vị của n
    return total

print('Tổng các chữ số của 12345:', sum_of_digits(12345))

# Bài 5: Viết một hàm find_max(numbers) để tìm vị trí số lớn nhất trong một danh sách numbers.
# 	YC1: Hàm nhận vào một danh sách các số nguyên.
# 	YC2: Hàm trả về vị trí số lớn nhất trong danh sách đó.
def find_max(arr):
    max_value = max(arr)        # Tìm giá trị lớn nhất của danh sách
    for i in range(len(arr)):   # Duyệt danh sách, cách 1 - có index, value
        if arr[i] == max_value: # Tìm vị trí của max_value
            return i            # Trả về vị trí
        
numbers = [10, 5, 1, 2, 6, 9999, 4, 9, 3, 7, 8]
print('Vị trí phần tử lớn nhất:', find_max(numbers))

# Bài 6: Viết một hàm sum_to_n(n) để tính tổng các số từ 1 đến n.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	Yc2: Hàm trả về tổng các số từ 1 đến n.
def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):   # Duyệt từ 1 đến n
        total += i              # Cộng i vào biến tổng
    return total                # Trả về tổng
print('Tổng các số từ 1 đến 10:', sum_to_n(10))