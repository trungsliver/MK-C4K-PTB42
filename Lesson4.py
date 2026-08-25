# # ===================== Luyện tập =====================
# # Câu 1: Nhập một số từ bàn phím và in ra số đó.
# number = input('Nhập 1 số bạn thích: ')
# print("Number: " + number)
# print("Number:", number)
# print(f"Number: {number}")

# # Câu 2: Viết chương trình kiểm tra nhập vào 1 số và kiểm tra số đó là chẵn hay lẻ.
# number = 36
# if number % 2 == 0:
#     print(number, "là số chẵn")
# else:
#     print(number, "là số lẻ")

# # Câu 3: Viết chương trình tính tổng, hiệu, tích, thương, chia lấy nguyên, chia lấy dư, lũy thừa của hai số nhập từ bàn phím.
# a = float(input("Nhập số a: "))
# b = float(input("Nhập số b: "))

# print("Tổng:", a + b)
# print("Hiệu:", a - b)
# print("Tích:", a * b)
# print("Lũy thừa:", a ** b)

# if b == 0:
#     print("Không thể chia cho 0")
# else:
#     print("Thương:", a / b)
#     print("Chia lấy nguyên:", a // b)
#     print("Chia lấy dư:", a % b)

# # Câu 4: Viết chương trình chuyển đổi từ USD sang VND (số tiền được nhập từ bàn phím).
# usd = float(input("Nhập số tiền USD: $"))
# vnd = usd * 26000
# print(f"${usd} = {vnd} VND")

# # Bài 5: Nhập số điện bạn sử dụng (kWh)
# # Tính tiền điện theo dữ liệu sau và hiển thị ra màn hình
# # Bậc 1:    0kWh - 50kWh           giá 1.8k VND / kWh
# # Bậc 2:    51kWh - 100kWh         giá 2k VND / kWh
# # Bậc 3:    101kWh - 200kWh        giá 2.3k VND / kWh
# # Bậc 4:    trên 201kWh            giá 3k VND / kWh

# # Nhập số điện sử dụng
# kWh = float(input("Nhập số điện sử dụng (kWh): "))
# # Biến lưu tổng tiền điện
# cash = 0

# # Tính tiền điện
# if 0 <= kWh <= 50:
#     cash = kWh * 1.8
# elif 51 <= kWh <= 100:
#     cash = 50 * 1.8 + (kWh - 50) * 2
# elif 101 <= kWh <= 200:
#     cash = 50 * 1.8 + 50 * 2 + (kWh - 100) * 2.3
# elif kWh > 200:
#     cash = 50 * 1.8 + 50 * 2 + 100 * 2.3 + (kWh - 200) * 3
# else:
#     print("Số điện không hợp lệ")

# # Hiển thị kết quả
# print(f"Tổng tiền điện: {cash} VND")

# # Bài 6: Nhập số giây
# # yêu cầu: Chuyển sang định dạng giờ phút giây
# # VD: 3661s = 1h 1m 1s

#     # Nhập dữ liệu
# time = int(input("Nhập số giây: "))
#     # Chuyển đổi
# hours = time // 3600
# minutes = (time % 3600) // 60
# seconds = time % 60
#     # Hiển thị kết quả
# print(f"{time}s = {hours}h {minutes}m {seconds}s")

# # Bài 7: Chia m cái kẹo cho n học sinh
# # Yêu cầu:
#     # Nhập m, n từ bàn phím
#     # Tính số kẹo mỗi học sinh được nhận
#     # Tính số kẹo còn lại sau khi chia

# m = int(input("Nhập số lượng kẹo: "))
# n = int(input("Nhập số lượng học sinh: "))
#     # Hiển thị kết quả
# print('Số kẹo học sinh nhận được:', m // n)
# print('Số kẹo còn thừa:', m % n)

# =============== Kiểm tra / Xử lý lỗi =================
    # Thử câu lệnh trong "try" trước
    # Nếu có lỗi thì sẽ nhảy sang "except" để xử lý lỗi
try:
    number = int(input("Nhập 1 số nguyên: "))
except:
    print("Bạn phải nhập 1 số nguyên")

