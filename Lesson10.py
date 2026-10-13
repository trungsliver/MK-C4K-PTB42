# String methods - các phương thức xử lý chuỗi
name = "Viet Cuong"

# len() - độ dài chuỗi / số lượng ký tự của chuỗi
print("Độ dài:", len(name))         # 10

# Ký tự thứ n trong string: string[n]
print("Ký tự đầu tiên:", name[0])      
print("Ký tự cuối cùng:", name[-1])
print("Ký tự 'C':", name[5])

# Duyệt string
    # Cách 1: Dùng cả index và value
for i in range(len(name)):
    print("Ký tự thứ", i, ":", name[i])

    # Cách 2: Dùng value
for char in name:
    print("Ký tự:", char)

# Xâu con (substring)
str1 = 'LeKhuong'
str2 = 'Khuong'
str3 = 'DepTrai'

    # Kiểm tra xâu con: in
print(str2 in str1)      # True
print(str3 in str1)      # False

    # Tìm vị trí xâu con: find()
print(str1.find(str2))      # 2
print(str1.find(str3))      # -1 (không tìm thấy)

# Slicing - cắt chuỗi
name = 'NguyenVuHaiDang'
    # Cắt vị trí bất kì
print(name[6:11])        # VuHai
    # Cắt từ đầu đến vị trí bất kì
print(name[:6])          # Nguyen
    # Cắt từ vị trí bất kì đến cuối
print(name[11:])            

# strip(): xóa khoảng trắng ở đầu và cuối chuỗi
str1 = '    Thanh Phong        '
print('Trước strip():', str1)
print('Sau strip():', str1.strip())

# split(): tách chuỗi
    # tách theo khoảng trắng
str1 = '1 2 3 4 5 6 7 8 9'
arr1 = str1.split()
print('arr1:', arr1)

    # tách theo ký tự bất kì
str2 = 'a,b,c,d,e,f,g,h,i'
arr2 = str2.split(',')
print('arr2:', arr2)

# join() - nối chuỗi
arr = ['r','o','n','a','l','d','o']

str1 = ''.join(arr)        # nối không có khoảng trắng
print('str1:', str1)

str2 = '-'.join(arr)        # nối bằng dấu gạch ngang
print('str2:', str2)

# replace() - thay thế chuỗi
song = 'baby shark doo doo doo doo doo doo'
    # Thay thế toàn bộ
song1 = song.replace('doo', 'khương')
print('song1:', song1)
    # Thay thế 1 phần
song2 = song.replace('doo', 'khương', 3)
print('song2:', song2)

# Chuẩn hóa chuỗi:
name = 'cHu aN bInH'
    # lower() - chuyển về chữ thường
print('lower():', name.lower())
    # upper() - chuyển về chữ hoa
print('upper():', name.upper())
    # title() - Viết hoa chữ cái đầu tiên của mỗi từ
print('title():', name.title())

# Chuyển đổi kiểu dữ liệu trong danh sách
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    # Cách 1: 
num1 = []
for item in numbers:
    num1.append(int(item))
print('num1:', num1)

    # Cách 2: Dùng list comprehension
num2 = [int(item) for item in numbers]
print('num2:', num2)

# ------------------------- Luyện tập -----------------------
# Bài 1: Nhập 2 thông tin: họ, tên. In ra màn hình tên đầy đủ
ho = input('Nhập họ: ')
ten = input('Nhập tên: ')
    # cách 1: nối chuỗi
print('Tên đầy đủ:', ho + ' ' + ten)
    # Cách 2: dùng join()
arr = [ho, ten]
name1 = ' '.join(arr)
print('Tên đầy đủ:', name1)

# Bài 2: Nhập vào 1 xâu ký tự định dạng dd/mm/yyyy (01/08/2024)
    # Tách ngày, tháng, năm và hiển thị ra màn hình
date1 = input('Nhập ngày tháng năm (dd/mm/yyyy): ')

    # cách 1: dùng split()
arr = date1.split('/')
print(f'Ngày: {arr[0]}, Tháng: {arr[1]}, Năm: {arr[2]}')

    # cách 2: dùng replace() và slicing
date2 = date1.replace('/', ' tháng ', 1)
date2 = date2.replace('/', ' năm ', 1)
print('Ngày tháng năm:', date2)

# Bài 3: Nhập vào thông tin dạng username:password
    # kiểm tra xem thông tin vừa nhập có trùng với thông tin có sẵn
    # YC2: bắt người dùng nhập đến khi nào trùng username và password thì kết thúc