import numpy as np

# Đọc dữ liệu từ file efficiency.txt
with open('efficiency.txt', 'r') as f_efficiency:
    efficiency = [int(line.strip()) for line in f_efficiency]

# Đọc dữ liệu từ file shifts.txt
with open('shifts.txt', 'r') as f_shifts:
    shifts = [line.strip() for line in f_shifts]

# Chuyển list thành numpy array
np_shifts = np.array(shifts)
np_efficiency = np.array(efficiency)

# Tính hiệu suất trung bình cho ca 'Morning'
morning_efficiency = np_efficiency[np_shifts == 'Morning']
average_morning_efficiency = np.mean(morning_efficiency)

# Tính hiệu suất trung bình cho các ca khác (không phải 'Morning')
non_morning_efficiency = np_efficiency[np_shifts != 'Morning']
average_non_morning_efficiency = np.mean(non_morning_efficiency)

# In kết quả
print(f"Hiệu suất trung bình của ca 'Morning': {average_morning_efficiency}")
print(f"Hiệu suất trung bình của các ca khác: {average_non_morning_efficiency}")

