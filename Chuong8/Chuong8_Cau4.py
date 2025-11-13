from tkinter import *

# Hàm thêm ký tự vào biểu thức
def press(num):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + str(num))

# Hàm thực hiện phép tính
def equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, END)
        entry.insert(0, result)
    except ZeroDivisionError:
        entry.delete(0, END)
        entry.insert(0, "Không thể chia cho 0")
    except:
        entry.delete(0, END)
        entry.insert(0, "Lỗi cú pháp")

# Hàm xóa toàn bộ
def clear():
    entry.delete(0, END)

# Tạo cửa sổ chính
root = Tk()
root.title("Máy tính bỏ túi")
root.geometry("300x400")

# Entry hiển thị biểu thức
entry = Entry(root, width=16, font=("Arial", 24), bd=5, relief=SUNKEN, justify=RIGHT)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Danh sách các nút
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Tạo các nút
row_val = 1
col_val = 0
for button in buttons:
    if button == "=":
        b = Button(root, text=button, width=5, height=2, font=("Arial", 18), command=equal)
    else:
        b = Button(root, text=button, width=5, height=2, font=("Arial", 18), command=lambda x=button: press(x))
    b.grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Nút xóa
Button(root, text="C", width=5, height=2, font=("Arial", 18), command=clear).grid(row=row_val, column=0, columnspan=4, sticky="we", padx=5, pady=5)

root.mainloop()
