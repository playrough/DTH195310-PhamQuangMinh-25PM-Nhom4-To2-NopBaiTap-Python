import math

# Nhập n
n = int(input("Nhập số n: "))

# Khởi tạo giá trị ban đầu
S = 0

# Tính căn lồng nhau từ trong ra ngoài
for i in range(n):
    S = math.sqrt(2 + S)

# Xuất kết quả
print(f"S({n}) = {S}")
