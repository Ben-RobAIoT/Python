# Label
## 1. What (Cái gì?)
Label trong Tkinter là một widget dùng để hiển thị văn bản hoặc hình ảnh tĩnh trong giao diện người dùng.

## 2. Who (Ai?)
Lập trình viên Python hoặc người phát triển ứng dụng GUI sử dụng Tkinter để tạo giao diện.

## 3. When (Khi nào?)
Khi cần hiển thị thông tin tĩnh như tiêu đề, mô tả, nhãn hướng dẫn, hoặc hình ảnh trong cửa sổ ứng dụng.

## 4. Where (Ở đâu?)
Trong cửa sổ hoặc khung (Frame) của ứng dụng Tkinter, có thể đặt Label ở bất kỳ vị trí nào bằng các phương thức layout như pack(), grid(), hoặc place().

## 5. Why (Tại sao?)
Vì Label giúp người dùng dễ dàng nhận biết thông tin hoặc hướng dẫn, đồng thời làm cho giao diện trở nên trực quan và dễ sử dụng hơn.

## 6. How (Như thế nào?)
Tạo Label bằng cú pháp:
```python
from tkinter import *
root = Tk()
lbl = Label(root, text="Xin chào", font=("Arial", 14))
lbl.pack()
root.mainloop()
```
