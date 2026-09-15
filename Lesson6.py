# Vòng lặp hữu hạn - Vòng lặp for

# Cú pháp đầy đủ range(start, stop, step)
    # start: giá trị bắt đầu (không bắt buộc, mặc định = 0)
    # stop: giá trị kết thúc (bắt buộc)
    # step: bước nhảy (không bắt buộc, mặc định = 1)
# Lưu ý: chạy từ start đến stop-1

# TH1: range(start, stop, step)
# TH2: range(start, stop)
# TH3: range(stop)

# Ví dụ:
# range(5,10): 5 6 7 8 9
# range(2, 10, 2): 2 4 6 8
# range(-5): không chạy
# range(-10, -5): -10 -9 -8 -7 -6
# range(1): 0
# range(2,8,3): 2 5
# range(2): 0 1
# range(-5, 2): -5 -4 -3 -2 -1 0 1

# ===================== LUYỆN TẬP =====================
# Bài 1: Nhập 2 số nguyên a và b từ bàn phím.
# In ra các số nguyên trong khoảng [a, b]
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

for i in range(a, b + 1):
    print(i, end=" ")

# Bài 2: Nhập 2 số nguyên a và b từ bàn phím.
# In ra các số nguyên trong khoảng [a, b] nếu b >= a
# In ra các số nguyên trong khoảng [b, a] nếu a > b
a = int(input("\nNhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

if b >= a:
    for i in range(a, b + 1):
        print(i, end=" ")
else:
    for i in range(b, a + 1):
            print(i, end=" ")

# Bài 3: Nhập 1 số nguyên a trong khoảng [1, 10]
# In ra màn hình bảng cửu chương a
a = int(input('\nNhập a trong khoảng [1,10]: '))

if 1 <= a <= 10:
    for i in range(1, 11):
        print(f'{a} x {i} = {a*i}')
else:
    print("Nhập sai a, a phải nằm trong khoảng [1,10]")

# Bài 4: In ra màn hình bảng cửu chương từ 2 => 9
for a in range(2, 10):
    print("\nBảng cửu chương", a)
    for i in range(1, 11):
        print(f'{a} x {i} = {a*i}')

# ========= VÒNG LẶP WHILE - VÒNG LẶP VÔ HẠN ==============
# Vòng lặp while không biết trước số lần lặp, có thể chạy vô hạn

# Cú pháp: while <điều kiện>: <Khối lệnh>
# Vòng lặp while sẽ chạy đến khi điều kiện sai

# Đề bài: in ra các số trong khoảng [1, 5]
    # Dùng vòng lặp for
for i in range(1, 6):
    print(i, end=' ')

    # Dùng vòng lặp while
i = 1
while i <= 5:
    print(i, end=' ')
    # Tăng i lên 1 đơn vị
    i = i + 1   # i += 1

# Ví dụ: Nhập số nguyên n trong khoảng [0, 10]
# Nếu nhập sai (n<0 hoặc n>10) thì yêu cầu nhập lại
n = int(input('\nNhập số nguyên trong khoảng [1, 10]: '))
while n < 0 or n > 10:
    print('Bạn đã nhập sai! Vui lòng nhập lại!')
    n = int(input('\nNhập số nguyên trong khoảng [1, 10]: '))
print('Nhập n thành công!')