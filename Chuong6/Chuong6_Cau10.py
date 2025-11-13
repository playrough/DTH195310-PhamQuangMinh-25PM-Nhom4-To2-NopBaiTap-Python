def NhapMaTran(m, n):
    return [[int(input(f"Nhập A[{i}][{j}]: ")) for j in range(n)] for i in range(m)]

def CongMaTran(A, B):
    m = len(A)
    n = len(A[0])
    C = [[A[i][j] + B[i][j] for j in range(n)] for i in range(m)]
    return C

def HoanViMaTran(M):
    # Trao đổi hàng thành cột
    return [list(row) for row in zip(*M)]

# Ví dụ
m = int(input("Số hàng: "))
n = int(input("Số cột: "))

print("Nhập ma trận A:")
A = NhapMaTran(m, n)
print("Nhập ma trận B:")
B = NhapMaTran(m, n)

C = CongMaTran(A, B)
print("Ma trận A + B:")
for row in C:
    print(row)

print("Ma trận A hoán vị:")
for row in HoanViMaTran(A):
    print(row)
