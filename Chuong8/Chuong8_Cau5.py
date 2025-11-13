from tkinter import *
from tkinter import messagebox

# Hàm kiểm tra đăng nhập
def dang_nhap():
    user = entry_user.get()
    pwd = entry_pwd.get()
    
    # Ví dụ username và password cố định
    if user == "admin" and pwd == "12345":
        messagebox.showinfo("Thông báo", "Đăng nhập thành công!")
    else:
        messagebox.showerror("Thông báo", "Sai tên đăng nhập hoặc mật khẩu")

# Tạo cửa sổ chính
root = Tk()
root.title("Màn hình đăng nhập")
root.geometry("300x200")
root.resizable(False, False)

# Nhãn tiêu đề
Label(root, text="Đăng nhập hệ thống", font=("Arial", 16), fg="blue").pack(pady=10)

# Frame chứa username và password
frame = Frame(root)
frame.pack(pady=10)

# Username
Label(frame, text="Username:").grid(row=0, column=0, padx=5, pady=5)
entry_user = Entry(frame)
entry_user.grid(row=0, column=1, padx=5, pady=5)

# Password
Label(frame, text="Password:").grid(row=1, column=0, padx=5, pady=5)
entry_pwd = Entry(frame, show="*")
entry_pwd.grid(row=1, column=1, padx=5, pady=5)

# Nút đăng nhập
Button(root, text="Đăng nhập", width=15, command=dang_nhap).pack(pady=10)

# Nút thoát
Button(root, text="Thoát", width=15, command=root.quit).pack()

root.mainloop()
