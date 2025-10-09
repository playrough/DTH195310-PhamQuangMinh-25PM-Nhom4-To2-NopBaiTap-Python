def doc_so(n):
    # Bảng ánh xạ các chữ số thành từ ngữ
    so_to_chu = {
        0: "không",
        1: "một",
        2: "hai",
        3: "ba",
        4: "bốn",
        5: "năm",
        6: "sáu",
        7: "bảy",
        8: "tám",
        9: "chín",
    }

    # Tách các chữ số
    tens = n // 10  # Chữ số hàng chục
    ones = n % 10  # Chữ số hàng đơn vị

    # Nếu là số có 1 chữ số
    if n < 10:
        return so_to_chu[n]

    # Nếu là số có 2 chữ số
    if tens > 0:
        if ones == 0:
            return so_to_chu[tens] + " mươi"
        elif ones == 1:
            return so_to_chu[tens] + " mươi một"
        elif ones == 4:
            return so_to_chu[tens] + " mươi bốn"
        elif ones == 5:
            return so_to_chu[tens] + " mươi năm"
        elif ones == 6:
            return so_to_chu[tens] + " mươi sáu"
        elif ones == 7:
            return so_to_chu[tens] + " mươi bảy"
        elif ones == 8:
            return so_to_chu[tens] + " mươi tám"
        elif ones == 9:
            return so_to_chu[tens] + " mươi chín"



print("Chương trình đọc số")
number = int(input("Nhập số: "))


print(doc_so(number))