n = int(input("Nhập số lượng phần tử: "))
lst = []

for i in range(n):
    while True:
        num = int(input(f"Nhập số thứ {i+1}: "))
        if i == 0 or num > lst[i-1]:
            lst.append(num)
            break
        else:
            print("Số không hợp lệ, phải lớn hơn số trước đó, nhập lại.")

print("Dãy số tăng dần:", lst)
