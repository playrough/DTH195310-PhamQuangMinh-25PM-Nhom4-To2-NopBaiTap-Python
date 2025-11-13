from tkinter import *

# Hàm chuyển đổi Fahrenheit sang Celsius
def F_to_C():
    try:
        f = float(entry_F.get())
        c = (f - 32) * 5/9
        string_C.set(f"{c:.2f} °C")
    except ValueError:
        string_C.set("Vui lòng nhập số hợp lệ!")

# Tạo cửa sổ chính
root = Tk()
root.title("Chuyển độ F sang độ C")
root.geometry("350x200")

# Nhãn và Entry
Label(root, text="Nhập nhiệt độ F:", font=("Arial", 12)).pack(pady=10)
entry_F = Entry(root, font=("Arial", 12))
entry_F.pack()

# Nút chuyển đổi
Button(root, text="Chuyển sang C", command=F_to_C, font=("Arial", 12), fg="white", bg="green").pack(pady=10)

# Hiển thị kết quả
string_C = StringVar()
Label(root, textvariable=string_C, font=("Arial", 12), fg="red").pack(pady=10)

# Nút thoát
Button(root, text="Thoát", command=root.quit).pack(pady=5)

root.mainloop()
