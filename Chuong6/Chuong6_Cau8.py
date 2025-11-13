n = int(input("Nhập số lượng phần tử: "))
M = [float(input(f"M[{i}]: ")) for i in range(n)]

M.sort(reverse=True)
print("Dãy số giảm dần:", M)
