def sum1(n):
    s = 0
    while n > 0:
        s += 1
        n -= 1
    return s

def sum2():
    global val
    s = 0
    while val > 0:
        s += 1
        val -= 1
    return s

def sum3():
    s = 0
    for i in range(val, 0, -1):
        s += 1
    return s


# ---------------------------
# Trường hợp 1
# ---------------------------
def main():
    global val
    val = 5
    print(sum1(5))   # → 5 (sum1 dùng biến cục bộ, không đổi val)
    print(sum2())    # → 5 (sum2 dùng val=5, sau khi chạy xong val = 0)
    print(sum3())    # → 0 (vì val = 0 sau sum2)
main()
# ✅ Kết quả in ra:
# 5
# 5
# 0


# ---------------------------
# Trường hợp 2
# ---------------------------
def main():
    global val
    val = 5
    print(sum1(5))   # → 5 (val vẫn = 5)
    print(sum3())    # → 5 (vì val vẫn = 5)
    print(sum2())    # → 5 (dùng val = 5, sau khi chạy xong val = 0)
main()
# ✅ Kết quả in ra:
# 5
# 5
# 5


# ---------------------------
# Trường hợp 3
# ---------------------------
def main():
    global val
    val = 5
    print(sum2())    # → 5 (val ban đầu = 5, sau khi chạy xong val = 0)
    print(sum1(5))   # → 5 (dùng biến cục bộ, không ảnh hưởng val)
    print(sum3())    # → 0 (vì val hiện tại = 0)
main()
# ✅ Kết quả in ra:
# 5
# 5
# 0
