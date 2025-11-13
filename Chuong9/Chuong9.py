import numpy as np
from sklearn.linear_model import LinearRegression

# Dữ liệu đầu vào
# Chiều cao (cm)
X = np.array([147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]).reshape(-1, 1)
# Cân nặng (kg)
y = np.array([49, 50, 51, 54, 58, 59, 60, 62, 63, 64, 66, 67, 68])

# Khởi tạo mô hình hồi quy tuyến tính
model = LinearRegression()
# Huấn luyện mô hình
model.fit(X, y)

# Hiển thị hệ số hồi quy
print(f"Hệ số w_1 (slope) = {model.coef_[0]:.4f}")
print(f"Hệ số w_0 (intercept) = {model.intercept_:.4f}")

# Dự đoán cân nặng dựa vào chiều cao nhập từ người dùng
your_height = float(input("Nhập chiều cao của bạn (cm): "))
predicted_weight = model.predict([[your_height]])[0]

print(f"Chiều cao của bạn: {your_height} cm, dự đoán cân nặng: {predicted_weight:.2f} kg")
