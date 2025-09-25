# Câu 8: Các loại lỗi khi lập trình và cách bắt lỗi trong Python
# Các loại lỗi:

# Lỗi cú pháp (SyntaxError): sai cấu trúc mã.

# Lỗi logic (LogicError): sai kết quả, không báo lỗi.

# Lỗi khi chạy (RuntimeError): xảy ra khi chương trình đang chạy (chia 0, sai kiểu, v.v).

# Cách bắt lỗi:
# try:
#     a = int(input("Nhập số: "))
#     b = 10 / a
# except ZeroDivisionError:
#     print("Không được chia cho 0")
# except ValueError:
#     print("Bạn phải nhập số")
# finally:
#     print("Kết thúc chương trình")