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

import random
# Lấy ngẫu nhiên 1 số trong khoảng [1,100]
number = random.randint(0, 100)

# Biến số đếm số lần đoán của người chơi
count = 1