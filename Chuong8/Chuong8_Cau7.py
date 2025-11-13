from tkinter import *

# Hàm chuyển năm Dương lịch sang Âm lịch
def duong_to_am():
    try:
        nam_duong = int(entry_duong.get())
        can = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]
        chi = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]
        nam_can = can[(nam_duong + 6) % 10]  # công thức tính Can
        nam_chi = chi[(nam_duong + 8) % 12] # công thức tính Chi
        string_am.set(f"Năm Âm lịch: {nam_can} {nam_chi}")
    except ValueError:
        string_am.set("Vui lòng nhập số nguyên hợp lệ!")

# Tạo cửa sổ chính
root = Tk()
root.title("Chuyển Năm Dương Lịch sang Âm Lịch")
root.geometry("400x200")

# Nhãn và Entry
Label(root, text="Nhập năm Dương lịch:", font=("Arial", 12)).pack(pady=10)
entry_duong = Entry(root, font=("Arial", 12))
entry_duong.pack()

# Nút chuyển đổi
Button(root, text="Chuyển sang Âm lịch", command=duong_to_am, font=("Arial", 12), fg="white", bg="blue").pack(pady=10)

# Hiển thị kết quả
string_am = StringVar()
Label(root, textvariable=string_am, font=("Arial", 12), fg="red").pack(pady=10)

# Nút thoát
Button(root, text="Thoát", command=root.quit).pack(pady=5)

root.mainloop()
