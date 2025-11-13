import random

# Tập hợp giá trị có thể xuất hiện
possible_values = [4.5, 34, -1, 100, 0, 99]

# Sinh ngẫu nhiên nhiều lần để kiểm tra
found = set()
for _ in range(100000):
    n = random.randrange(0, 100)
    if n in possible_values:
        found.add(n)

print("Các giá trị có thể xuất hiện:", sorted(found))
