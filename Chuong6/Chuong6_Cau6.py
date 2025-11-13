from random import randint

N = int(input("Nhập số phần tử N: "))
lst = []

while len(lst) < N:
    num = randint(0, 100)
    if num not in lst:
        lst.append(num)

print("List ngẫu nhiên không trùng nhau:", lst)
