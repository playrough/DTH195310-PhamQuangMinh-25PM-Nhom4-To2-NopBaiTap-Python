print("Chương trình kiểm tra năm nhuần: ")
year = int(input("Nhập năm: "))

if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
    print("Năm nhuần!")
else:
    print("Năm không nhuần!")