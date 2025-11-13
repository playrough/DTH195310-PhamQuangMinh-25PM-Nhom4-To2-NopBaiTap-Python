def toi_uu_chuoi(s):
    # Loại bỏ khoảng trắng thừa, mỗi từ viết hoa chữ cái đầu
    s = s.strip()                   # Bỏ khoảng trắng đầu-cuối
    tu_list = s.split()             # Tách thành list các từ
    tu_list = [tu.capitalize() for tu in tu_list]  # Viết hoa chữ cái đầu mỗi từ
    return ' '.join(tu_list)

# Ví dụ
s = " TRần duY thAnH "
print(toi_uu_chuoi(s))  # Output: Trần Duy Thanh
