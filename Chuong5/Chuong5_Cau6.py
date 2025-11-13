import re

def NegativeNumberInStrings(s):
    # Tìm các số nguyên âm theo mẫu -số, ví dụ: -5, -12
    so_am = re.findall(r'-\d+', s)
    print("Các số nguyên âm trong chuỗi:", so_am)

# Ví dụ
NegativeNumberInStrings("abc-5xyz-12k9l--p")
