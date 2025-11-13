lst = [3, 0, 1, 5, 2]
x = 2

print("a)", lst[0])        # 3
print("b)", lst[3])        # 5
print("c)", lst[x])        # lst[2] = 1
print("d)", lst[-x])       # lst[-2] = 5
print("e)", lst[x+1])      # lst[3] = 5
print("f)", lst[x] + 1)    # 1 + 1 = 2
print("g)", lst[lst[x]])   # lst[lst[2]] = lst[1] = 0
print("h)", lst[lst[lst[x]]])  # lst[lst[lst[2]]] = lst[lst[1]] = lst[0] = 3
