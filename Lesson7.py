# ========= VÒNG LẶP WHILE - VÒNG LẶP VÔ HẠN ==============
# Vòng lặp while không biết trước số lần lặp, có thể chạy vô hạn

# Cú pháp: while <điều kiện>: <Khối lệnh>
# Vòng lặp while sẽ chạy đến khi điều kiện sai

# Bài 1: Dùng vòng lặp while in ra các số trong khoảng [5, 12]
i = 5
while i <= 12:
    print(i, end = ' ')
    i += 1

# Bài 2: Nhập số nguyên n trong khoảng [0, 100]
# Nếu nhập sai (n<0 hoặc n>100) thì yêu cầu nhập lại
n = int(input("\nNhập số nguyên n trong khoảng [0,100]: "))

while n < 0 or n > 100:
    print("Bạn đã nhập sai! Vui lòng nhập lại!")
    n = int(input("\nNhập số nguyên n trong khoảng [0,100]: "))
print('Nhập n thành công!')

# Bài 3: Tạo Mysterious Game
    # Yêu cầu: tạo ra 1 số đặc biệt để đoán (random)
    # Người chơi cần nhập đến khi nào đoán đúng số đặc biệt thì dừng game
    # Khi người chơi đoán đúng, hiển thị số lần người chơi đã đoán

# import random
# # Lấy ngẫu nhiên 1 số trong khoảng [1,100]
# number = random.randint(0, 100)

# # Biến số đếm số lần đoán của người chơi
# count = 1

# # Người chơi nhập dự đoán
# guess = int(input('\nNhập dự đoán của bạn: '))

# while guess != number:
#     if guess < number:
#         print('Chưa đúng. Hãy nhập số lớn hơn')
#     if guess > number:
#         print('Chưa đúng. Hãy nhập số nhỏ hơn')
#     # Tăng số lần đoán thêm 1 và cho nhập lại
#     count += 1
#     guess = int(input('\nNhập dự đoán của bạn: '))
# print(f'Bạn đã đoán đúng sau {count} lần thử')

# ========= CÂU LỆNH ĐIỀU KHIỂN VÒNG LẶP ===========
    # break: thoát khỏi vòng lặp, bỏ qua tất cả lần lặp còn lại
print('\nTest câu lệnh break')
for i in range(1, 11):
    if i == 5:
        break
    print(i, end = ' ')

    # continue: bỏ qua lần lặp hiện tại, tiếp tục các lần lặp tiếp theo
print('\nTest câu lệnh continue')
for i in range(1, 11):
    if i == 5:
        continue
    print(i, end = ' ')

# ================= ÔN TẬP VÒNG LẶP FOR ==================
# Dạng 1: In / hiển thị ra màn hình
    # 1.1. In ra màn hình các số từ 0 đến n
n = 10
print(f'\nCác số trong khoảng [0, {n}]: ')
for i in range(n+1):
    print(i, end=' ')

    # 1.2. In ra màn hình các số nguyên trong khoảng [a, b]
a = 5
b = 10
print(f'\nCác số trong khoảng [{a}, {b}]: ')
for i in range(a, b+1):
    print(i, end=' ')

    # 1.3. In ra màn hình các số chẵn trong khoảng [a, b]
a = 1
b = 10
print(f'\nCác số chẵn trong khoảng [{a}, {b}]: ')
for i in range(a, b+1):
    if i % 2 == 0:
        print(i, end=' ')

    # 1.4. In ra màn hình các số lẻ trong khoảng [a, b]
a = 1
b = 10
print(f'\nCác số lẻ trong khoảng [{a}, {b}]: ')
for i in range(a, b+1):
    if i % 2 != 0:
        print(i, end=' ')

# Dạng 2: Tính tổng
    # 2.1. Tính tổng các số trong khoảng [a, b]
a, b = 1, 5
total = 0       # Biến lưu tổng các số
for i in range(a, b+1):
    # Cộng dồn các số vào total
    total += i      # totatl = total + i
print(f'\nTổng các số trong khoảng [{a}, {b}] là: {total}')

    # 2.2. Tính tổng các số chẵn trong khoảng [a, b]
a, b = 1, 5
total_even = 0       # Biến lưu tổng các số
for i in range(a, b+1):
    if i % 2 == 0:
        total_even += i      # total_even = total_even + i
print(f'\nTổng các số chẵn trong khoảng [{a}, {b}] là: {total_even}')

    # 2.3. Tính tổng các số lẻ trong khoảng [a, b]
a, b = 1, 5
total_odd = 0      
for i in range(a, b+1):
    if i % 2 != 0:
        total_odd += i      
print(f'\nTổng các số lẻ trong khoảng [{a}, {b}] là: {total_odd}')

# Dạng 3: Đếm số lượng
    # 3.1. Đếm số lượng các số chẵn trong khoảng [a, b]
a, b = 0, 10
count_even = 0
for i in range(a, b+1):
    if i % 2 == 0:
        count_even += 1
print(f'\nSố lượng các số chẵn trong khoảng [{a}, {b}] là: {count_even}')

    # 3.2. Đếm số lượng số lẻ trong khoảng [a,b]
a, b = 1, 10
count_odd = 0
for i in range(a, b+1):
    if i % 2 != 0:
        count_odd += 1
print(f'\nSố lượng các số lẻ trong khoảng [{a}, {b}] là: {count_odd}')