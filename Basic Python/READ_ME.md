# 🐍 Các cách sử dụng hàm `print()` trong Python

Hàm `print()` trong Python được dùng để xuất dữ liệu ra màn hình hoặc file.  
Dưới đây là tổng hợp các cách sử dụng thường gặp, kèm ví dụ và kết quả.

---

## 1. Cơ bản nhất
```python
print("Hello, world!")
Kết quả:

Copy
Edit
Hello, world!
2. In nhiều giá trị cùng lúc
python
Copy
Edit
print("Họ:", "Nguyễn", "Văn", "A")
Kết quả:

less
Copy
Edit
Họ: Nguyễn Văn A
3. Thay đổi ký tự phân tách (sep)
python
Copy
Edit
print("2025", "08", "11", sep="-")
Kết quả:

yaml
Copy
Edit
2025-08-11
4. Không xuống dòng sau khi in (end)
python
Copy
Edit
print("Hello", end=" ")
print("world")
Kết quả:

nginx
Copy
Edit
Hello world
5. Dùng f-string (Python 3.6+)
python
Copy
Edit
name = "Tín"
age = 20
print(f"Tôi tên {name}, {age} tuổi")
Kết quả:

css
Copy
Edit
Tôi tên Tín, 20 tuổi
6. Dùng .format()
python
Copy
Edit
print("Tôi tên {}, {} tuổi".format(name, age))
print("Tôi tên {1}, {0} tuổi".format(age, name))
Kết quả:

css
Copy
Edit
Tôi tên Tín, 20 tuổi
Tôi tên Tín, 20 tuổi
7. Dùng toán tử % (cũ nhưng vẫn gặp)
python
Copy
Edit
print("Tôi tên %s, %d tuổi" % (name, age))
Kết quả:

css
Copy
Edit
Tôi tên Tín, 20 tuổi
8. In nhiều dòng
python
Copy
Edit
print("""Dòng 1
Dòng 2
Dòng 3""")
Kết quả:

mathematica
Copy
Edit
Dòng 1
Dòng 2
Dòng 3
9. In kèm biểu thức
python
Copy
Edit
a, b = 5, 3
print("Tổng:", a + b)
print(f"{a} + {b} = {a + b}")
Kết quả:

makefile
Copy
Edit
Tổng: 8
5 + 3 = 8
10. In sang file
python
Copy
Edit
with open("output.txt", "w", encoding="utf-8") as f:
    print("Ghi vào file thay vì màn hình", file=f)
📄 Nội dung file output.txt:

nginx
Copy
Edit
Ghi vào file thay vì màn hình
✍ Tác giả: [Tên của bạn]
📅 Ngày cập nhật: 2025-08-11

yaml
Copy
Edit

---

Nếu bạn muốn, mình có thể hướng dẫn **cách push file README.md này lên GitHub** sao cho repo hiển thị đẹp như một trang tài liệu Python mini.  
Bạn có muốn mình làm luôn hướng dẫn push lên GitHub không?
