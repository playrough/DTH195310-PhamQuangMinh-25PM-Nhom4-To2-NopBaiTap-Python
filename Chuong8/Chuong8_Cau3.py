from tkinter import *

def congAction():
    try:
        a = float(stringA.get())
        b = float(stringB.get())
        stringKQ.set(a + b)
    except ValueError:
        stringKQ.set("Vui lòng nhập số hợp lệ")

def truAction():
    try:
        a = float(stringA.get())
        b = float(stringB.get())
        stringKQ.set(a - b)
    except ValueError:
        stringKQ.set("Vui lòng nhập số hợp lệ")

def nhanAction():
    try:
        a = float(stringA.get())
        b = float(stringB.get())
        stringKQ.set(a * b)
    except ValueError:
        stringKQ.set("Vui lòng nhập số hợp lệ")

def chiaAction():
    try:
        a = float(stringA.get())
        b = float(stringB.get())
        if b == 0:
            stringKQ.set("Không thể chia cho 0")
        else:
            stringKQ.set(a / b)
    except ValueError:
        stringKQ.set("Vui lòng nhập số hợp lệ")

root = Tk()
root.title("Cộng Trừ Nhân Chia")
root.minsize(height=180, width=250)

stringA = StringVar()
stringB = StringVar()
stringKQ = StringVar()

Label(root, text="Cộng Trừ Nhân Chia", fg="blue", font=("Tahoma", 16)).grid(row=0, columnspan=3)

# Khung các nút chức năng
frameButton = Frame(root)
Button(frameButton, text="Cộng", command=congAction).pack(side=TOP, fill=X)
Button(frameButton, text="Trừ", command=truAction).pack(side=TOP, fill=X)
Button(frameButton, text="Nhân", command=nhanAction).pack(side=TOP, fill=X)
Button(frameButton, text="Chia", command=chiaAction).pack(side=TOP, fill=X)
frameButton.grid(row=1, column=0, rowspan=4, padx=5, pady=5)

# Nhập số a, số b và hiển thị kết quả
Label(root, text="Số a:").grid(row=1, column=1)
Entry(root, width=15, textvariable=stringA).grid(row=1, column=2)
Label(root, text="Số b:").grid(row=2, column=1)
Entry(root, width=15, textvariable=stringB).grid(row=2, column=2)
Label(root, text="Kết quả:").grid(row=3, column=1)
Entry(root, width=15, textvariable=stringKQ, state='readonly').grid(row=3, column=2)

# Nút thoát
Button(root, text="Thoát", command=root.quit).grid(row=4, column=2, pady=5)

root.mainloop()
