✍ **Tác giả:** [Phan Bao Tin - Beniot]  
📅 **Ngày cập nhật:** {{DATE}}  

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
# 🐍 Bài tập Python cơ bản: `print()` và Ghi chú

## 🎯 Mục tiêu
- Làm quen với lệnh **`print()`** để xuất dữ liệu ra màn hình.
- Hiểu và sử dụng các loại **ghi chú** trong Python:
  - Ghi chú một dòng (Single-line comment)
  - Ghi chú nhiều dòng (Multi-line comment)
  - Docstring (Documentation String)

---

## 📂 Cấu trúc bài tập
Bài tập được chia làm **5 phần** theo mức độ từ cơ bản đến nâng cao.

---

## **Phần 1: Làm quen với `print()`**

**Bài 1:** In ra dòng chữ: Xin chào Python

**Bài 2:** In ra tên và tuổi của bạn.  
Ví dụ: Tên tôi là Tín, tôi 20 tuổi

**Bài 3:** In ra 3 câu chào khác nhau, mỗi câu trên một dòng.

**Bài 4:** In ra một đoạn văn nhiều dòng bằng **một lệnh `print()`** (gợi ý: dùng `\n` để xuống dòng).

**Bài 5:** In kết quả phép tính `25 + 17` bằng `print()`.

---

## **Phần 2: Ghi chú một dòng (Single-line comment)**

**Bài 6:** Viết chương trình in ra tên bạn, trong đó:
- Dòng đầu tiên ghi chú mô tả mục đích chương trình.
- Mỗi lệnh `print()` có ghi chú giải thích chức năng.

**Bài 7:** Viết chương trình in ra diện tích hình chữ nhật (width = 5, height = 3), kèm ghi chú giải thích từng bước tính toán.

---

## **Phần 3: Ghi chú nhiều dòng (Multi-line comment)**

**Bài 8:** Viết chương trình in ra bảng cửu chương của số 5.  
Phần đầu file dùng **ghi chú nhiều dòng** để mô tả:
- Tác giả
- Ngày viết
- Mục tiêu chương trình

**Bài 9:** Viết chương trình in ra họ tên, năm sinh, quê quán của bạn, phần đầu dùng **chuỗi nhiều dòng `''' ... '''`** làm ghi chú.

---

## **Phần 4: Docstring**

**Bài 10:** Viết hàm `greet(name)` in ra câu chào với tên truyền vào.
- Dùng **docstring** để mô tả hàm (mục đích, tham số, giá trị trả về).
- Gọi hàm và in ra docstring của hàm.

**Bài 11:** Viết hàm `add(a, b)` trả về tổng hai số, kèm docstring mô tả.
- In kết quả của `add(10, 20)`
- In ra docstring bằng `print(add.__doc__)`

---

## **Phần 5: Kết hợp**

**Bài 12:**  
Viết chương trình:
- Dùng **ghi chú nhiều dòng** để mô tả chương trình.
- Dùng **ghi chú một dòng** giải thích từng bước.
- In ra:
  1. Họ tên
  2. Năm sinh
  3. Phép tính 15 × 7
  4. Một đoạn văn nhiều dòng bằng `print()` và ký tự `\n`.

---

## 💡 Gợi ý khi làm bài
1. Luôn chạy thử để kiểm tra kết quả.
2. Dùng ghi chú để giải thích *tại sao* bạn viết lệnh đó.
3. Thử kết hợp `print()` với toán tử `+` hoặc `,` để nối chuỗi.
4. Khi dùng docstring cho hàm/lớp, có thể truy cập bằng cú pháp:
   ```python
   print(tên_hàm.__doc__)


