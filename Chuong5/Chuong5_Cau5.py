def dem_ky_tu(s):
    in_hoa = in_thuong = chu_so = ky_tu_dac_biet = khoang_trang = nguyen_am = phu_am = 0
    nguyen_am_set = set('aeiouAEIOU')
    
    for c in s:
        if c.isupper():
            in_hoa += 1
        if c.islower():
            in_thuong += 1
        if c.isdigit():
            chu_so += 1
        if c.isspace():
            khoang_trang += 1
        if c.isalpha():
            if c in nguyen_am_set:
                nguyen_am += 1
            else:
                phu_am += 1
        if not (c.isalnum() or c.isspace()):
            ky_tu_dac_biet += 1

    print("Chữ IN HOA:", in_hoa)
    print("Chữ in thường:", in_thuong)
    print("Chữ số:", chu_so)
    print("Ký tự đặc biệt:", ky_tu_dac_biet)
    print("Khoảng trắng:", khoang_trang)
    print("Nguyên âm:", nguyen_am)
    print("Phụ âm:", phu_am)

# Ví dụ
chuoi = input("Nhập chuỗi: ")
dem_ky_tu(chuoi)
