✍ **Tác giả:** [Phan Bao Tin - Beniot]  
📅 **Ngày cập nhật:** 2025-08-11  

# Bài 2 – PHẦN MỀM TÍNH ĐIỂM TRUNG BÌNH CỘNG

## 🎯 Kiến thức cần đạt:
- Hiểu cách tính điểm trong Thế vận hội Đông Nam Á.
- Sử dụng biến, các kiểu dữ liệu.
- Sử dụng toán tử gán và toán tử số học.
- Biết cách sử dụng `input()` và lệnh ghi chú (`#`).
- Lập trình phần mềm tính điểm TBC.

## 🛠️ Kỹ năng cần đạt:
- Biết cách sử dụng biến, toán tử gán và toán tử số học.
- Hiểu về các kiểu dữ liệu trong Python.
- Biết cách áp dụng `input()` để giải quyết các bài toán thực tiễn.

---

## 📚 Lý thuyết

### 1. Biến và kiểu dữ liệu
- **Biến**: dùng để lưu trữ giá trị tạm thời trong chương trình.
- **Các kiểu dữ liệu cơ bản** trong Python:
  - `int` – số nguyên
  - `float` – số thực
  - `str` – chuỗi ký tự

Ví dụ:
```python
so_nguyen = 5       # int
so_thuc = 3.14      # float
chuoi = "Hello"     # str
```

### 2. Toán tử gán và toán tử số học
- **Toán tử gán (`=`)**: gán giá trị cho biến.
- **Toán tử số học**:
  - `+` cộng
  - `-` trừ
  - `*` nhân
  - `/` chia (kết quả float)
  - `//` chia lấy nguyên
  - `%` chia lấy dư
  - `**` lũy thừa

Ví dụ:
```python
a = 10
b = 3
tong = a + b       # 13
thuong = a / b     # 3.333...
```

### 3. Hàm `input()`
- Dùng để nhập dữ liệu từ bàn phím.
- Giá trị nhập vào luôn là kiểu `str`, cần ép kiểu khi làm tính toán.

Ví dụ:
```python
diem = float(input("Nhập điểm: "))
```

### 4. Công thức tính điểm trung bình cộng
Trong SEA Games, điểm trung bình cộng thường được tính bằng:
```
TBC = (Tổng điểm) / (Số môn thi)
```

---

## 📌 Ví dụ minh họa
```python
# Chương trình tính điểm trung bình cộng
print("=== TÍNH ĐIỂM TRUNG BÌNH CỘNG ===")

# Nhập dữ liệu
mon1 = float(input("Nhập điểm môn 1: "))
mon2 = float(input("Nhập điểm môn 2: "))
mon3 = float(input("Nhập điểm môn 3: "))

# Tính TBC
tbc = (mon1 + mon2 + mon3) / 3

# Xuất kết quả
print("Điểm trung bình cộng là:", round(tbc, 2))
```

---

## 🎯 Bài tập luyện tập

### Bài 1:
Viết chương trình nhập điểm 5 môn học và in ra điểm trung bình.

### Bài 2:
Viết chương trình tính điểm trung bình của vận động viên trong 4 môn thi đấu.  
Yêu cầu:
- Nhập tên vận động viên.
- Nhập điểm từng môn.
- Xuất tên và điểm trung bình.

### Bài 3 (nâng cao):
Viết chương trình tính điểm trung bình của N môn học (N nhập từ bàn phím).

