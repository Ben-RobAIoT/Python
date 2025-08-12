✍ **Tác giả:** [Phan Bao Tin - Beniot]  
📅 **Ngày cập nhật:** 2025-08-11  

# Bài 5 – PHẦN MỀM XẾP LOẠI HỌC SINH

## 🎯 Kiến thức cần đạt
- Hiểu cách phân chia cấp bậc trong giáo dục Việt Nam.
- Tìm hiểu về cấu trúc rẽ nhánh trong lập trình.
- Làm quen với các câu lệnh: `if – else`; `if – elif – else`.

## 🛠 Kỹ năng cần đạt
- Hiểu được cấu trúc rẽ nhánh.
- Biết sử dụng các câu lệnh `if – else`; `if – elif – else`.
- Biết ứng dụng cấu trúc rẽ nhánh để giải quyết các bài toán thực tiễn.

---

## 📚 Lý thuyết

### 1. Cấu trúc rẽ nhánh `if – else`
Cú pháp:
```python
if điều_kiện:
    # Khối lệnh nếu điều_kiện đúng
else:
    # Khối lệnh nếu điều_kiện sai
```

Ví dụ:
```python
diem = 8
if diem >= 5:
    print("Đậu")
else:
    print("Rớt")
```

---

### 2. Cấu trúc rẽ nhánh nhiều nhánh `if – elif – else`
Cú pháp:
```python
if điều_kiện_1:
    # Khối lệnh nếu điều_kiện_1 đúng
elif điều_kiện_2:
    # Khối lệnh nếu điều_kiện_2 đúng
elif điều_kiện_3:
    # Khối lệnh nếu điều_kiện_3 đúng
else:
    # Khối lệnh nếu không điều_kiện nào đúng
```

Ví dụ:
```python
diem = 7
if diem >= 8:
    print("Giỏi")
elif diem >= 6.5:
    print("Khá")
elif diem >= 5:
    print("Trung bình")
else:
    print("Yếu")
```

---

## 📊 Thang đánh giá học lực (theo ví dụ)
- **Giỏi**: Điểm trung bình ≥ 8.0
- **Khá**: 6.5 ≤ Điểm trung bình < 8.0
- **Trung bình**: 5.0 ≤ Điểm trung bình < 6.5
- **Yếu**: Điểm trung bình < 5.0

---

## 💡 Bài tập ví dụ: Xếp loại học sinh
```python
# Nhập điểm trung bình
diem_tb = float(input("Nhập điểm trung bình của học sinh: "))

# Xếp loại
if diem_tb >= 8:
    print("Xếp loại: Giỏi")
elif diem_tb >= 6.5:
    print("Xếp loại: Khá")
elif diem_tb >= 5:
    print("Xếp loại: Trung bình")
else:
    print("Xếp loại: Yếu")
```

---

## 📝 Bài tập tự luyện
1. Viết chương trình nhập điểm của học sinh và xếp loại theo thang đánh giá ở trên.
2. Viết chương trình nhập điểm toán, lý, hóa và tính điểm trung bình, sau đó xếp loại.
3. Viết chương trình xếp loại học sinh nhưng bổ sung thêm hạng "Xuất sắc" cho điểm ≥ 9.0.
4. Viết chương trình yêu cầu nhập thêm hạnh kiểm (Tốt, Khá, Trung bình, Yếu) và chỉ xếp loại Giỏi nếu hạnh kiểm Tốt.
5. Viết chương trình xếp loại học lực dựa trên nhiều môn học và hiển thị danh sách học sinh theo thứ tự từ cao đến thấp.

---

## 🚀 Gợi ý mở rộng
- Tạo phần mềm quản lý nhiều học sinh (lưu vào danh sách hoặc file).
- Kết hợp cấu trúc rẽ nhánh với vòng lặp để xử lý nhiều dữ liệu cùng lúc.
- Thêm chức năng tìm kiếm học sinh theo tên hoặc mã số.

