import os

def lay_ten_file_duong_dan(duong_dan):
    # Lấy tên file kèm phần mở rộng
    return os.path.basename(duong_dan)

def lay_ten_bai_hat(duong_dan):
    # Lấy tên file không phần mở rộng
    ten_file = os.path.basename(duong_dan)
    ten_bai_hat = os.path.splitext(ten_file)[0]
    return ten_bai_hat

# Ví dụ
duong_dan = r'd:\music\muabui.mp3'

print("Tên file:", lay_ten_file_duong_dan(duong_dan))  # muabui.mp3
print("Tên bài hát:", lay_ten_bai_hat(duong_dan))      # muabui
