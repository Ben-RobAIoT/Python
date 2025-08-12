✍ **Tác giả:** [Phan Bao Tin - Beniot]  
📅 **Ngày cập nhật:** 2025-08-11  

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

# Cách ghi chú trong Python
Có 2 kiểu ghi chú trong Python
1) Ghi chú trên 1 dòng  [Single-line comment]
    - Kí tự: **#**
    - Giải thích: Mọi thứ sau **#** chương trình sẽ không thực thi
    - Ví dụ:
```python
a = int(input("Nhập số nguyên vào đây: ") # Gán 1 biến a với kiểu là dữ liệu nhập vào là một số nguyên
```
**Kết quả:**
Không hiển thị bất kì đoạn mã nào liên quan tới (Gán 1 biến **a** với kiểu là dữ liệu **nhập vào** là một **số nguyên**)
```
Nhập số nguyên vào đây: 
```

2) Ghi chú nhiều dòng [Multiple-line comment]
    - Cách 1: Sử dụng nhiều ghi chú 1 dòng **#**
```python
# Dòng ghi chú 1
# Dòng ghi chú 2
# Dòng ghi chú 3
```
```
    - Cách 2: Sử dụng kí tự """...""" hoặc '''...'''
```python
'''
Đây là ghi chú nhiều dòng
Nó sẽ bị bỏ qua khi không được gán cho biến
'''
```
3) Docstring (Document string)
    - Dùng """ ... """ hoặc ''' ... '''
    - Khác với ghi chú thường, docstring được lưu trong thuộc tính .__doc__ của hàm/lớp/module → hỗ trợ tài liệu hoá.

```python
def hello(name):
    """
    Hàm hello
    Tham số:
        name (str): Tên người dùng
    Trả về:
        None
    """
    print(f"Xin chào {name}")

print(hello.__doc__)
```
---
# Bài tập thực hành


