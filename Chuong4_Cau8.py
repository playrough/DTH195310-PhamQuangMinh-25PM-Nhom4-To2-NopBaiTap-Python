import math

# Nhập giá trị a và x
a = float(input("Nhập cơ số a: "))
x = float(input("Nhập số x: "))

# Kiểm tra điều kiện hợp lệ
if a <= 0 or a == 1:
    print("Cơ số a phải > 0 và khác 1.")
elif x <= 0:
    print("Giá trị x phải > 0.")
else:
    # Tính log_a(x)
    logax = math.log(x) / math.log(a)
    print(f"log_{a}({x}) = {logax}")
