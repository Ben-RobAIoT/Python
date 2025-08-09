students = []

FIELDS = ["Họ và tên", "MSSV", "Lớp", "Năm sinh", "Giáo viên", "Phụ huynh", "SĐT phụ huynh"]

def print_header():
    print("{:<20} {:<10} {:<15} {:<10} {:<15} {:<20} {:<15}".format(*FIELDS))

def input_student_info():
    return [input(f"Nhập {f}: ") for f in FIELDS]

def display(students_list=None):
    if not students_list:
        print("Danh sách học sinh trống.")
        return
    print_header()
    for s in students_list:
        print("{:<20} {:<10} {:<15} {:<10} {:<15} {:<20} {:<15}".format(*s))

def add():
    print("\n--- Thêm học sinh ---")
    students.append(input_student_info())
    print(">>>>> Thêm học sinh mới thành công <<<<<")
    display([students[-1]])

def erase():
    print("\n--- Xóa học sinh ---")
    if not students: return print("Danh sách trống.")
    mssv = input("Nhập MSSV: ")
    for s in students:
        if s[1] == mssv:
            students.remove(s)
            print(f"Đã xóa MSSV {mssv} thành công!")
            return display(students)
    print(f"Không tìm thấy MSSV {mssv}.")

def find():
    print("\n--- Tìm kiếm học sinh ---")
    if not students: return print("Danh sách trống.")
    mssv = input("Nhập MSSV: ")
    for s in students:
        if s[1] == mssv:
            return display([s])
    print(f"Không tìm thấy MSSV {mssv}.")

def modify():
    print("\n--- Sửa thông tin học sinh ---")
    if not students: return print("Danh sách trống.")
    mssv = input("Nhập MSSV: ")
    for s in students:
        if s[1] == mssv:
            while True:
                display([s])
                try:
                    idx = int(input("Chọn số trường muốn sửa (1-7): ")) - 1
                    if 0 <= idx < len(FIELDS):
                        s[idx] = input(f"Nhập {FIELDS[idx]} mới: ")
                    else:
                        print("Không hợp lệ.")
                except ValueError:
                    print("Nhập số.")
                if input("Sửa tiếp? (Y/N): ").upper() != "Y":
                    break
            return
    print(f"Không tìm thấy MSSV {mssv}.")

def system():
    while True:
        print("\nChọn chức năng: [a] Thêm | [m] Sửa | [e] Xóa | [f] Tìm | [d] Hiển thị | exit")
        cmd = input("> ").lower()
        if cmd == "exit":
            print("Thoát hệ thống.")
            break
        {"a": add, "m": modify, "e": erase, "f": find, "d": lambda: display(students)}.get(cmd, lambda: print("Sai cú pháp"))()

if input("***Nhập cú pháp 'STD_INFO' để truy cập: ") == "STD_INFO":
    system()
else:
    for i in range(4):
        print(f"Bạn còn {3-i} lần thử.")
        if input("Nhập lại cú pháp: ") == "STD_INFO":
            system()
            break
    else:
        print("Hết lượt thử, vui lòng tải lại.")

