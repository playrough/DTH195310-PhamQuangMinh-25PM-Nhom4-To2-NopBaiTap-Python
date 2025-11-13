lst = [20, 1, -34, 40, -8, 60, 1, 3]

print("a)", lst)         # [20, 1, -34, 40, -8, 60, 1, 3]
print("b)", lst[0:3])    # [20, 1, -34]
print("c)", lst[4:8])    # [-8, 60, 1, 3]
print("d)", lst[4:33])   # [-8, 60, 1, 3]  # slice vượt quá độ dài list
print("e)", lst[-5:-3])  # [40, -8]
print("f)", lst[-22:3])  # [20, 1, -34]  # slice âm vượt quá list
print("g)", lst[4:])     # [-8, 60, 1, 3]
print("h)", lst[:])      # copy list đầy đủ
print("i)", lst[:4])     # [20, 1, -34, 40]
print("j)", lst[1:5])    # [1, -34, 40, -8]
print("k)", -34 in lst)  # True
print("l)", -34 not in lst)  # False
print("m)", len(lst))    # 8
