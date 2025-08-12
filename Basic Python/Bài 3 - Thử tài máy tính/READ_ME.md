✍ **Tác giả:** [Phan Bao Tin - Beniot]  
📅 **Ngày cập nhật:** 2025-08-11  

# Bài 3 – THỬ TÀI MÁY TÍNH

## 🎯 Kiến thức cần đạt
- Hiểu cách chơi và quy tắc của môn cờ vua.
- Làm quen vòng lặp `for`.
- Sử dụng vòng lặp để tối ưu hóa trong lập trình.

## 🛠 Kỹ năng cần đạt
- Biết cách sử dụng vòng lặp `for`.
- Biết ứng dụng vòng lặp trong vấn đề thực tế.
- Biết ứng dụng vòng lặp để giải quyết các bài toán thực tiễn.

---

## 📚 Lý thuyết

### 1. Vòng lặp `for` trong Python
Cú pháp cơ bản:
```python
for biến in dãy:
    # khối lệnh được lặp
```

Ví dụ:
```python
for i in range(5):
    print("Lần lặp thứ", i)
```

### 2. Hàm `range()`
- `range(n)`: tạo dãy số từ 0 đến n-1.
- `range(a, b)`: tạo dãy số từ a đến b-1.
- `range(a, b, step)`: tạo dãy số từ a đến b-1, bước nhảy là `step`.

Ví dụ:
```python
for i in range(2, 10, 2):
    print(i)  # In ra các số chẵn từ 2 đến 8
```

---

## 💡 Bài tập ví dụ

### Ví dụ 1: Đếm từ 1 đến 10
```python
for i in range(1, 11):
    print(i)
```

### Ví dụ 2: Tính tổng các số từ 1 đến n
```python
n = int(input("Nhập số nguyên dương n: "))
tong = 0
for i in range(1, n + 1):
    tong += i
print("Tổng từ 1 đến", n, "là:", tong)
```

### Ví dụ 3: Bảng cửu chương
```python
n = int(input("Nhập số cần in bảng cửu chương: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
```

---

## 📝 Bài tập tự luyện

1. Viết chương trình in ra tất cả các số lẻ từ 1 đến 100.
2. Viết chương trình tính tích của các số từ 1 đến n.
3. Viết chương trình tính tổng các số chẵn từ 1 đến n.
4. Viết chương trình in ra bảng cửu chương từ 2 đến 9.
5. Viết chương trình đếm ngược từ 10 về 1.

---

## 🚀 Gợi ý mở rộng
- Ứng dụng vòng lặp `for` để mô phỏng các trò chơi như đoán số, cờ vua, hoặc kiểm tra số nguyên tố.
- Kết hợp với `if` để xử lý điều kiện trong từng vòng lặp.

