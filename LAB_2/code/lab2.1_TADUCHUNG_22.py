import numpy as np

# Tạo mảng nhiệt độ ngẫu nhiên từ 10 đến 35 độ C
temperature_data = np.random.uniform(10, 35, 30)

# Làm tròn nhiệt độ đến 2 chữ số sau dấu phẩy
temperature_data = np.round(temperature_data, 2)

# In mảng nhiệt độ
print("Dữ liệu nhiệt độ:", temperature_data)

# Tính nhiệt độ trung bình trong tháng
avg_temperature = np.mean(temperature_data)
print("Nhiệt độ trung bình trong tháng:", avg_temperature)


# Tìm ngày có nhiệt độ cao nhất và thấp nhất
highest_temp = np.max(temperature_data)
lowest_temp = np.min(temperature_data)

day_highest = np.argmax(temperature_data) + 1  # Cộng thêm 1 vì chỉ mục bắt đầu từ 0
day_lowest = np.argmin(temperature_data) + 1

print(f"Nhiệt độ cao nhất: {highest_temp} vào ngày {day_highest}")
print(f"Nhiệt độ thấp nhất: {lowest_temp} vào ngày {day_lowest}")

# Thống kê sự chênh lệch nhiệt độ giữa các ngày
temperature_diff = np.abs(np.diff(temperature_data))  # Lấy giá trị tuyệt đối của sự khác biệt

# Tìm ngày có sự biến đổi nhiệt độ lớn nhất
max_diff_day = np.argmax(temperature_diff) + 1  # Thêm 1 vì np.diff giảm chiều dài mảng đi 1
max_diff_value = np.max(temperature_diff)

print(f"Sự biến đổi nhiệt độ lớn nhất là {max_diff_value} vào ngày {max_diff_day}")

# Tất cả các ngày có nhiệt độ cao hơn 20 độ C
days_above_20 = np.where(temperature_data > 20)[0] + 1  # Thêm 1 vì chỉ mục bắt đầu từ 0
print(f"Ngày có nhiệt độ trên 20 độ C: {days_above_20}")

# Lấy nhiệt độ của ngày 5, 10, 15, 20, 25
days_to_check = [5, 10, 15, 20, 25]
temperatures_on_selected_days = temperature_data[days_to_check - 1]  # Trừ 1 vì chỉ mục bắt đầu từ 0
print(f"Nhiệt độ của ngày 5, 10, 15, 20, 25: {temperatures_on_selected_days}")

# Nhiệt độ của các ngày có nhiệt độ trên trung bình
days_above_avg = np.where(temperature_data > avg_temperature)[0] + 1
temperatures_above_avg = temperature_data[days_above_avg - 1]
print(f"Nhiệt độ của các ngày có nhiệt độ trên trung bình: {temperatures_above_avg}")

# Lấy nhiệt độ của các ngày chẵn/lẻ trong tháng
even_days_temperatures = temperature_data[1::2]  # Ngày chẵn (chỉ mục lẻ)
odd_days_temperatures = temperature_data[0::2]   # Ngày lẻ (chỉ mục chẵn)

print(f"Nhiệt độ các ngày chẵn: {even_days_temperatures}")
print(f"Nhiệt độ các ngày lẻ: {odd_days_temperatures}")
