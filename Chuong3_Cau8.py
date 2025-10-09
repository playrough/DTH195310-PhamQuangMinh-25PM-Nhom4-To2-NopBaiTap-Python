def cal(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b != 0:
            return a / b
        else:
            return "Lỗi: Không thể chia cho 0"
    else:
        return "Lỗi: Phép toán không hợp lệ"


# Nhập giá trị a, b và phép toán op
a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
op = input("Nhập phép toán (+, -, *, /): ")

# Tính và xuất kết quả
result = cal(a, b, op)
print(f"Kết quả: {result}")
