import numpy as np
import csv

# Đọc dữ liệu từ file CSV
efficiency_data = []
with open('Data/diem_hoc_phan.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Bỏ qua dòng header
    for row in reader:
        efficiency_data.append(row[2:5])  # Chỉ lấy dữ liệu điểm của HP1, HP2, HP3

# Chuyển đổi dữ liệu điểm thành mảng NumPy
diem_hp = np.array(efficiency_data, dtype=float)

# Hiển thị mảng NumPy
print("Dữ liệu điểm số dưới dạng mảng NumPy:")
print(diem_hp)

def qui_doi_diem(diem):
    if diem >= 8.5:
        return 'A'
    elif diem >= 8.0:
        return 'B+'
    elif diem >= 7.0:
        return 'B'
    elif diem >= 6.5:
        return 'C+'
    elif diem >= 5.5:
        return 'C'
    elif diem >= 5.0:
        return 'D+'
    elif diem >= 4.0:
        return 'D'
    else:
        return 'F'

# Áp dụng qui đổi cho tất cả điểm trong mảng diem_hp
diem_tinchi = np.vectorize(qui_doi_diem)(diem_hp)

# In kết quả
print("\nĐiểm tín chỉ cho các học phần:")
print(diem_tinchi)

# Chia tách dữ liệu theo từng học phần
hp1 = diem_hp[:, 0]  # Điểm học phần 1
hp2 = diem_hp[:, 1]  # Điểm học phần 2
hp3 = diem_hp[:, 2]  # Điểm học phần 3

# In kết quả
print("\nĐiểm học phần 1:", hp1)
print("Điểm học phần 2:", hp2)
print("Điểm học phần 3:", hp3)

# Phân tích tổng, trung bình và độ lệch chuẩn cho từng học phần
tongs_hp1 = np.sum(hp1)
tongs_hp2 = np.sum(hp2)
tongs_hp3 = np.sum(hp3)

avg_hp1 = np.mean(hp1)
avg_hp2 = np.mean(hp2)
avg_hp3 = np.mean(hp3)

std_hp1 = np.std(hp1)
std_hp2 = np.std(hp2)
std_hp3 = np.std(hp3)

# In kết quả
print(f"\nTổng điểm học phần 1: {tongs_hp1}, Trung bình: {avg_hp1}, Độ lệch chuẩn: {std_hp1}")
print(f"Tổng điểm học phần 2: {tongs_hp2}, Trung bình: {avg_hp2}, Độ lệch chuẩn: {std_hp2}")
print(f"Tổng điểm học phần 3: {tongs_hp3}, Trung bình: {avg_hp3}, Độ lệch chuẩn: {std_hp3}")

from collections import Counter

# Chuyển đổi các điểm tín chỉ thành mảng 1 chiều
flat_diem_tinchi = diem_tinchi.flatten()

# Tính số lượng sinh viên đạt mỗi loại điểm chữ
counter = Counter(flat_diem_tinchi)

# In kết quả
print("\nSố lượng sinh viên đạt mỗi loại điểm chữ:")
for grade, count in counter.items():
    print(f"{grade}: {count}")
