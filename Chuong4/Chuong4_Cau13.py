# Hàm tính tổng các ước số (không kể chính nó)
def tong_uoc_so(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:   # Nếu i là ước của n
            tong += i
    return tong


# a) Kiểm tra số hoàn thiện
def la_so_hoan_thien(n):
    return tong_uoc_so(n) == n


# b) Kiểm tra số thịnh vượng
def la_so_thinh_vuong(n):
    return tong_uoc_so(n) > n


# ---------------------------
# Chương trình chính
# ---------------------------
n = int(input("Nhập số nguyên dương n: "))

if la_so_hoan_thien(n):
    print(f"{n} là số hoàn thiện.")
elif la_so_thinh_vuong(n):
    print(f"{n} là số thịnh vượng.")
else:
    print(f"{n} không phải là số hoàn thiện hay thịnh vượng.")
