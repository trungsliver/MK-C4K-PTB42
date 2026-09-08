# Quy tắc đặt tên file: [Lớp]_[Hoten]_CP1.py
# Ví dụ: PTB42_DucTrung_CP1.py

# Link đề bài: shorturl.at/SrrPL

# Hạn nộp: 20h10

# Trắc nghiệm
# 1A 2B 3C 4D ...

# Tự luận
# ............

# Trừ điểm:
# An Bình: 1
# Việt Cường: 1

# ================= Vấn đáp =================:
# Thanh Phong: 0/3 + 1 điểm xung phong
# Duy Khôi: 1.5/3
# Khánh Nam:
# An Bình: 1/3
# Lê Khương: 1/3
# Việt Cường: 1.5/3
# Hải Đăng: 2.5/3

# ================ VÒNG LẶP FOR ================
# Vòng lặp hữu hạn - biết trước số lần lặp

# Cú pháp đầy đủ: range(start, stop, step)
    # start: giá trị bắt đầu (không bắt buộc, mặc định là 0)
    # stop: giá trị kết thúc (bắt buộc)
    # step: bước nhảy (không bắt buộc, mặc định là 1)
# Lưu ý: range() chạy từ start đến stop - 1, không bao gồm stop

# TH1: range(start, stop, step)
for i in range(1, 10, 2):
    print(i)
    print('Việt Cường đang hát')

# TH2: range(start, stop)
for i in range(1, 10):  # range(1, 10, 1)
    print(i)

# TH3: range(stop)
for i in range(5):  # range(0, 5, 1)
    print(i)
