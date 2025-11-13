from tkinter import *
from tkinter import ttk

# Tạo cửa sổ chính
root = Tk()
root.title("Demo Style Button")
root.geometry("400x300")

# Nhãn tiêu đề
Label(root, text="Các kiểu Button với ttk.Style", font=("Arial", 14), fg="blue").pack(pady=10)

# Tạo style
style = ttk.Style()
style.theme_use('default')  # Sử dụng theme mặc định

# Tạo các style khác nhau
style.configure('Red.TButton', foreground='white', background='red', font=('Arial', 12, 'bold'))
style.configure('Green.TButton', foreground='white', background='green', font=('Arial', 12))
style.configure('Blue.TButton', foreground='white', background='blue', font=('Arial', 12, 'italic'))

# Frame chứa các nút
frame = Frame(root)
frame.pack(pady=20)

# Button với các style khác nhau
ttk.Button(frame, text="Button Red", style='Red.TButton').grid(row=0, column=0, padx=10, pady=10)
ttk.Button(frame, text="Button Green", style='Green.TButton').grid(row=0, column=1, padx=10, pady=10)
ttk.Button(frame, text="Button Blue", style='Blue.TButton').grid(row=0, column=2, padx=10, pady=10)

# Nút thoát
Button(root, text="Thoát", command=root.quit).pack(pady=10)

root.mainloop()
