# Nhập số lượng học sinh
so_hoc_sinh = int(input("Nhập số lượng học sinh: "))
hoc_sinh_arr = {}
diem_arr =  {}
hoc_luc_arr = {}

# Duyệt từng học sinh
for i in range(so_hoc_sinh):
    print(f"\nHọc sinh thứ {i+1}")
    học_sinh = input("Nhập tên học sinh: ")
    diem = float(input("Nhập điểm trung bình: "))

    hoc_sinh_arr[i] = học_sinh
    diem_arr[i] = diem

    # Xếp loại học lực
    if diem >= 8.0:
        hoc_luc = "Giỏi quá - " + hoc_sinh_arr[i]
    elif diem >= 6.5:
        hoc_luc = "Làm tốt lắm - " + hoc_sinh_arr[i]
    elif diem >= 5.0:
        hoc_luc = "Cố gắng hơn nữa nhé - "  + hoc_sinh_arr[i]
    else:
        hoc_luc = "Cần tập trung hơn nhé - "  + hoc_sinh_arr[i]

    hoc_luc_arr[i] = hoc_luc
    # In kết quả

print("\nTổng kết lớp học")

for i in range(so_hoc_sinh):
    print(hoc_luc_arr[i])
