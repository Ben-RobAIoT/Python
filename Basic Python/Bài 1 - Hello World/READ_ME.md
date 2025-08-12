# 🐍 Các cách sử dụng hàm `print()` trong Python

Hàm `print()` trong Python được dùng để xuất dữ liệu ra màn hình hoặc file.  
Dưới đây là tổng hợp các cách sử dụng thường gặp, kèm ví dụ và kết quả.

---

## 1. Cơ bản nhất
```python
print("Hello, world!")
```
**Kết quả:**
```
Hello, world!
```

---

## 2. In nhiều giá trị cùng lúc
```python
print("Họ:", "Nguyễn", "Văn", "A")
```
**Kết quả:**
```
Họ: Nguyễn Văn A
```

---

## 3. Thay đổi ký tự phân tách (`sep`)
```python
print("2025", "08", "11", sep="-")
```
**Kết quả:**
```
2025-08-11
```

---

## 4. Không xuống dòng sau khi in (`end`)
```python
print("Hello", end=" ")
print("world")
```
**Kết quả:**
```
Hello world
```

---

## 5. Dùng f-string (Python 3.6+)
```python
name = "Tín"
age = 20
print(f"Tôi tên {name}, {age} tuổi")
```
**Kết quả:**
```
Tôi tên Tín, 20 tuổi
```

---

## 6. Dùng `.format()`
```python
print("Tôi tên {}, {} tuổi".format(name, age))
print("Tôi tên {1}, {0} tuổi".format(age, name))
```
**Kết quả:**
```
Tôi tên Tín, 20 tuổi
Tôi tên Tín, 20 tuổi
```

---

## 7. Dùng toán tử `%` (cũ nhưng vẫn gặp)
```python
print("Tôi tên %s, %d tuổi" % (name, age))
```
**Kết quả:**
```
Tôi tên Tín, 20 tuổi
```

---

## 8. In nhiều dòng
```python
print("""Dòng 1
Dòng 2
Dòng 3""")
```
**Kết quả:**
```
Dòng 1
Dòng 2
Dòng 3
```

---

## 9. In kèm biểu thức
```python
a, b = 5, 3
print("Tổng:", a + b)
print(f"{a} + {b} = {a + b}")
```
**Kết quả:**
```
Tổng: 8
5 + 3 = 8
```

---

## 10. In sang file
```python
with open("output.txt", "w", encoding="utf-8") as f:
    print("Ghi vào file thay vì màn hình", file=f)
```
📄 Nội dung file `output.txt`:
```
Ghi vào file thay vì màn hình
```

---

✍ **Tác giả:** [Phan Bao Tin - Beniot]  
📅 **Ngày cập nhật:** 2025-08-11  

