def CheckPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

M = [3,6,7,8,11,17,2,90,2,5,4,5,8]

# Số lẻ
le = [x for x in M if x % 2 != 0]
print("Số lẻ:", le, "Tổng số:", len(le))

# Số chẵn
chan = [x for x in M if x % 2 == 0]
print("Số chẵn:", chan, "Tổng số:", len(chan))

# Số nguyên tố
nt = [x for x in M if CheckPrime(x)]
print("Số nguyên tố:", nt)

# Không phải số nguyên tố
k_nt = [x for x in M if not CheckPrime(x)]
print("Không phải số nguyên tố:", k_nt)
