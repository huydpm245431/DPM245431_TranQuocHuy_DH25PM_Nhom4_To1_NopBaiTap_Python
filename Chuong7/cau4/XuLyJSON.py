# XuLyJSON.py - Chuyển JSON String → Python Object
import json

# Chuỗi JSON (phải hợp lệ)
jsonString = '{ "ma":"nv1", "age":50, "ten":"Trần Duy Thanh"}'

# Chuyển thành Python Object (Dictionary)
dataObject = json.loads(jsonString)

# In toàn bộ object
print("Dữ liệu JSON sau khi chuyển:")
print(dataObject)
print("-" * 40)

# Truy cập từng trường
print(f"Mã nhân viên: {dataObject['ma']}")
print(f"Tên: {dataObject['ten']}")
print(f"Tuổi: {dataObject['age']}")

# Bonus: Dùng vòng lặp in đẹp
print("\nIn bằng vòng lặp:")
for key, value in dataObject.items():
    print(f"{key.capitalize()}: {value}")