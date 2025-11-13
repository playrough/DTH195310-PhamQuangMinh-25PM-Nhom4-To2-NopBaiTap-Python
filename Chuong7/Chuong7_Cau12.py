import csv, random

# Ghi CSV
with open('random10x10.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    for _ in range(10):
        row = [random.randint(0,100) for _ in range(10)]
        writer.writerow(row)

# Đọc CSV và tính tổng mỗi dòng
with open('random10x10.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        total = sum(int(x) for x in row)
        print("Dòng:", row, "Tổng:", total)
