#  cv=2*π*r và dt=π*r*r

import math

try:
    r = float(input("Moi ban nhap ban kinh hinh tron: "))
    cv = 2*math.pi*r
    dt = math.pi*r*r
    print("Chu vi = ", cv)
    print("Dien tich = ", dt)
except:
    print("Lỗi rồi!")