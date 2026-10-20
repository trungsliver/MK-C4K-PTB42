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

# Bài 2: Viết một hàm is_prime(n) để kiểm tra xem một số nguyên dương n có phải là số nguyên tố hay không.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	YC2: Hàm trả về True nếu n là số nguyên tố, ngược lại trả về False.

# Bài 3: Viết một hàm count_words(s) để đếm số lượng từ trong một chuỗi s.
# 	YC1: Hàm nhận vào một chuỗi ký tự s.
# 	YC2: Hàm trả về số lượng từ trong chuỗi đó.

# Bài 4: Viết một hàm sum_of_digits(n) để tính tổng các chữ số của một số nguyên dương n.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	YC2: Hàm trả về tổng các chữ số của n.

# Bài 5: Viết một hàm find_max(numbers) để tìm vị trí số lớn nhất trong một danh sách numbers.
# 	YC1: Hàm nhận vào một danh sách các số nguyên.
# 	YC2: Hàm trả về vị trí số lớn nhất trong danh sách đó.

# Bài 6: Viết một hàm sum_to_n(n) để tính tổng các số từ 1 đến n.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	Yc2: Hàm trả về tổng các số từ 1 đến n.