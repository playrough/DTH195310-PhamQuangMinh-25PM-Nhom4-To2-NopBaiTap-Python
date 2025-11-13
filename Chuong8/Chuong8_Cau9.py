from tkinter import *

# Hàm tính BMI và xác định tình trạng cân nặng
def tinh_BMI():
    try:
        height = float(entry_height.get())  # Chiều cao (m)
        weight = float(entry_weight.get())  # Cân nặng (kg)
        if height <= 0 or weight <= 0:
            string_result.set("Chiều cao và cân nặng phải > 0!")
            return
        bmi = weight / (height ** 2)
        # Xác định tình trạng cân nặng
        if bmi < 18.5:
            status = "Gầy"
        elif 18.5 <= bmi <= 24.9:
            status = "Bình thường"
        elif 25 <= bmi <= 29.9:
            status = "Mập"
        else:
            status = "Béo phì"
        string_result.set(f"BMI = {bmi:.2f} → {status}")
    except ValueError:
        string_result.set("Vui lòng nhập số hợp lệ!")

# Hàm xóa dữ liệu
def xoa_du_lieu():
    entry_height.delete(0, END)
    entry_weight.delete(0, END)
    string_result.set("")

# Cửa sổ chính
root = Tk()
root.title("Phần mềm tính BMI")
root.geometry("400x250")

# Nhãn và Entry nhập chiều cao
Label(root, text="Chiều cao (m):", font=("Arial", 12)).pack(pady=5)
entry_height = Entry(root, font=("Arial", 12))
entry_height.pack()

# Nhãn và Entry nhập cân nặng
Label(root, text="Cân nặng (kg):", font=("Arial", 12)).pack(pady=5)
entry_weight = Entry(root, font=("Arial", 12))
entry_weight.pack()

# Nút tính BMI
Button(root, text="Tính BMI", command=tinh_BMI, font=("Arial", 12), fg="white", bg="blue").pack(pady=10)

# Nút xóa
Button(root, text="Xóa", command=xoa_du_lieu, font=("Arial", 12), fg="white", bg="red").pack(pady=5)

# Hiển thị kết quả
string_result = StringVar()
Label(root, textvariable=string_result, font=("Arial", 12), fg="green").pack(pady=10)

# Nút thoát
Button(root, text="Thoát", command=root.quit, font=("Arial", 12)).pack(pady=5)

root.mainloop()
