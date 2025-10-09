def kiem_tra_nhuan(nam):
    # Kiểm tra năm nhuận
    if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
        return True
    return False


def ngay_ke_tiep(ngay, thang, nam):
    # Các tháng có 31 ngày
    thang_31 = [1, 3, 5, 7, 8, 10, 12]
    # Các tháng có 30 ngày
    thang_30 = [4, 6, 9, 11]

    # Kiểm tra nếu tháng 12, chuyển sang tháng 1 của năm sau
    if thang == 12 and ngay == 31:
        nam += 1
        thang = 1
        ngay = 1
    # Nếu tháng có 31 ngày
    elif thang in thang_31 and ngay == 31:
        thang += 1
        ngay = 1
    # Nếu tháng có 30 ngày
    elif thang in thang_30 and ngay == 30:
        thang += 1
        ngay = 1
    # Xử lý tháng 2
    elif thang == 2:
        if kiem_tra_nhuan(nam) and ngay == 29:  # Năm nhuận, tháng 2 có 29 ngày
            thang += 1
            ngay = 1
        elif (
            not kiem_tra_nhuan(nam) and ngay == 28
        ):  # Năm không nhuận, tháng 2 có 28 ngày
            thang += 1
            ngay = 1
        elif (
            kiem_tra_nhuan(nam) and ngay == 28
        ):  # Nếu ngày trong tháng 2 là 28 và năm nhuận
            ngay += 1
    # Nếu là ngày hợp lệ trong các tháng còn lại
    elif ngay < 31:
        ngay += 1
    else:
        thang += 1
        ngay = 1

    # Nếu tháng 13, tăng năm và reset tháng về 1
    if thang == 13:
        thang = 1
        nam += 1

    return ngay, thang, nam


# Nhập ngày, tháng, năm từ người dùng
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

ngay_tiep, thang_tiep, nam_tiep = ngay_ke_tiep(ngay, thang, nam)

print(f"Ngày kế tiếp là: {ngay_tiep}/{thang_tiep}/{nam_tiep}")
