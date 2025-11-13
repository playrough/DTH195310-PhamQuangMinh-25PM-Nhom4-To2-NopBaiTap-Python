def oscillate(a, b):
    for i in range(a, b):
        yield i
        yield -i

# Kiểm tra kết quả
for n in oscillate(-3, 5):
    print(n, end=' ')
print()
