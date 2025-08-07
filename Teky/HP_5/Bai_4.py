# Vẽ hình vuông
n = int(input("Nhập kích thước hình vuông: "))

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

# Vẽ tam giác vuông
n = int(input("Nhập chiều cao tam giác: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()
  
# Vẽ tam giác ngược
n = int(input("Nhập chiều cao tam giác ngược: "))

for i in range(n, 0, -1):
    for j in range(i):
        if j == 2:
            continue  # Bỏ qua vị trí thứ 3 mỗi hàng
        print("*", end=" ")
    print()
