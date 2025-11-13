from random import randrange

print("Chương trình xử lý List")
n = int(input("Nhập số phần tử: "))
lst = [0] * n

# Khởi tạo list với các số ngẫu nhiên trong khoảng -100 đến 99
for i in range(n):
    lst[i] = randrange(-100, 100)

print("List ngẫu nhiên là:")
print(lst)

# Thêm số mới vào list
print("Mời bạn thêm số mới:")
value = int(input())
lst.append(value)
print(lst)

# Đếm số xuất hiện trong list
print("Bạn muốn đếm số nào:")
k = int(input())
dem = lst.count(k)
print(k, "xuất hiện", dem, "lần trong list")

# Hàm kiểm tra số nguyên tố
def CheckPrime(n):
    if n < 2:
        return False
    d = 0
    for i in range(1, n + 1):
        if n % i == 0:
            d += 1
    return d == 2

# Đếm và tính tổng các số nguyên tố trong list
demnt = 0
tongnt = 0
for x in lst:
    if CheckPrime(x):
        demnt += 1
        tongnt += x

print("Có", demnt, "số nguyên tố trong list")
print("Tổng =", tongnt)

# Sắp xếp list
lst.sort()
print("List sau khi sort:")
print(lst)

# Xóa list
del lst
print("List đã bị xóa, không thể in được nữa!")
