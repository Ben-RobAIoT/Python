student_list_infor = [] # Tạo 1 danh sách thông tin của học sinh
exit_event = True

teacher_mail_list = [
    "VuTriVien@tdtu.edu.vn",
    "TranDucAnhMinh@tdtu.edu.vn"
    "NguyenThanhQuang@tdtu.edu.vn"
]
teacher_pass_list = [
    "123456",
    "abcdef",
    "098765"
]

# Hiển thị các chữ cái dưới dạng chữ kiểu
logo_all = { # Kiểu cấu trúc dạng dictionary, trong đó các danh sách được lồng vào và tượng trưng là mỗi key
    "A": [
        "  *  ",
        " * * ",
        "*****",
        "*   *",
        "*   *",
        "*   *"
    ],
    "B": [
        "**** ",
        "*   *",
        "**** ",
        "*   *",
        "*   *",
        "**** "
    ],
    "C": [
        " ****",
        "*    ",
        "*    ",
        "*    ",
        "*    ",
        " ****"
    ],
    "E": [
        "     ",
        "*****",
        "*    ",
        "*****",
        "*    ",
        "*****"
    ],
    "H": [
        "*   *",
        "*   *",
        "*****",
        "*   *",
        "*   *",
        "*   *"
    ],
    "I": [
        "*****",
        "  *  ",
        "  *  ",
        "  *  ",
        "  *  ",
        "*****"
    ],
    "K": [
        "     ",
        "*   *",
        "*  * ",
        "**   ",
        "*  * ",
        "*   *"
    ],
    "N": [
        "*   *",
        "**  *",
        "* * *",
        "*  **",
        "*   *",
        "*   *"
    ],
    "O": [
        " *** ",
        "*   *",
        "*   *",
        "*   *",
        "*   *",
        " *** "
    ],
    "P": [
        "**** ",
        "*   *",
        "**** ",
        "*    ",
        "*    ",
        "*    "
    ],
    "T": [
        "*****",
        "  *  ",
        "  *  ",
        "  *  ",
        "  *  ",
        "  *  "
    ],
    "Y": [
        "     ",
        "*   *",
        " * * ",
        "  *  ",
        "  *  ",
        "  *  "
    ],
    " ": [
        "     ",
        "     ",
        "     ",
        "     ",
        "     ",
        "     "
    ]
}

def Add_tool(): # Hàm THÊM thông tin học sinh mới
    Apperance_tool("a")
    name = input("Nhập tên học sinh: ")
    id_student = input("Nhập MSSV: ")
    id_class = input("Nhập tên lớp học: ")
    birth = input("Nhập năm sinh: ")
    teacher = input("Nhập tên giáo viên: ")
    parent = input("Nhập tên phụ huynh: ")
    parent_num = input("Nhập sdt phụ huynh: ")
    student_list_infor.append([name, id_student, id_class, birth, teacher, parent, parent_num])
    last_student = student_list_infor[-1]

    print ("====================================================================")
    GUI("list")
    
    print ("{:<20} {:<10} {:<15} {:<10} {:<15} {:<20} {:<15}".format(last_student[0],
                                                                    last_student[1],
                                                                    last_student[2],
                                                                    last_student[3],
                                                                    last_student[4],
                                                                    last_student[5],
                                                                    last_student[6]
                                                                    ))
    print(">>>>> Thêm học sinh mới THÀNH CÔNG <<<<<")
    print ("====================================================================")

def Erase_tool(): # Hàm xóa thông tin của học sinh
    Apperance_tool("e")
    if not student_list_infor:
        print("Danh sách học sinh đang trống.")
        return # Nếu không tồn tại học sinh nào để thực hiện chức năng XÓA thì sẽ trả về biến rỗng để tiếp tục hỏi trong hàm Student_system, tương tự các chức năng m, f

    id_student = input("Nhập MSSV của học sinh cần xóa: ")

    found = False
    for student in student_list_infor:
        if student[1] == id_student:
            student_list_infor.remove(student)
            found = True
            print(f">>>>> Đã xóa học sinh MSSV {id_student} thành công! <<<<<")
            print("Danh sách CẬP NHẬT lại")
            Show_tool()
            break

    if not found:
        print(f"Không tìm thấy học sinh có MSSV {id_student}.")
    
def Find_tool(): # Hàm TÌM KIẾM thông tin của học sinh
    Apperance_tool("f")
    if not student_list_infor:
        print("Danh sách học sinh đang trống.")
        return
    
    id_student = input("Nhập MSSV của học sinh cần HIỂN THỊ: ")

    found = False
    for student in student_list_infor:
        if student[1] == id_student:
            found = True

            print(f"Thông tin của HS có MSSV: {id_student}.")
            print ("====================================================================")
            GUI("list")
            
            print ("{:<20} {:<10} {:<15} {:<10} {:<15} {:<20} {:<15}".format(student[0],
                                                                            student[1],
                                                                            student[2],
                                                                            student[3],
                                                                            student[4],
                                                                            student[5],
                                                                            student[6]
                                                                            ))
            break

    if not found:
        print(f"Không tìm thấy học sinh có MSSV {id_student}.")

def Modify_tool(): # Hàm TÙY CHỈNH thông tin của học sinh
    Apperance_tool("m")
    if not student_list_infor:
        print("Danh sách học sinh đang trống.")
        return
    
    id_student = input("Nhập MSSV của học sinh cần TÙY CHỈNH: ")

    found = False
    for student in student_list_infor:
        if student[1] == id_student:
            while True:
                found = True
                GUI()
                print ("Chọn thông tin cần chỉnh sửa theo form phía trên")
                print ("Thông tin học sinh NGUYÊN BẢN [trước khi chỉnh sửa]")
                GUI("list")
                
                print ("{:<20} {:<10} {:<15} {:<10} {:<15} {:<20} {:<15}".format(student[0],
                                                                student[1],
                                                                student[2],
                                                                student[3],
                                                                student[4],
                                                                student[5],
                                                                student[6]
                                                                ))
                modify_tool = int(input("Vui lòng hãy nhập số tương ứng [VD: 1,2,3,....]: ")) 
                if (modify_tool == 1):
                    student[0] = input("Nhập LẠI tên học sinh: ")
                elif (modify_tool == 2):
                    student[1] = input("Nhập LẠI MSSV: ")
                elif (modify_tool == 3):
                    student[2] = input("Nhập LẠI tên lớp học: ")
                elif (modify_tool == 4):
                    student[3] = input("Nhập LẠI năm sinh: ")
                elif (modify_tool == 5):
                    student[4] = input("Nhập LẠI tên giáo viên: ")
                elif (modify_tool == 6):
                    student[5] = input("Nhập LẠI tên phụ huynh: ")
                elif (modify_tool == 7):
                    student[6] = input("Nhập LẠI sdt phụ huynh: ")
                else:
                    print("Cú pháp yêu cầu của bạn KHÔNG ĐÚNG theo hướng dẫn")
                    print("Vui lòng nhập lại theo trên")

                print ("Thông tin học sinh THAY ĐỔI [sau khi chỉnh sửa]")                
                print ("{:<20} {:<10} {:<15} {:<10} {:<15} {:<20} {:<15}".format("1.Họ và tên", 
                                                                    "2.MSSV", 
                                                                    "3.Lớp", 
                                                                    "4.Năm sinh", 
                                                                    "5.Giáo viên", 
                                                                    "6.Phụ huynh", 
                                                                    "7.SĐT phụ huynh"
                                                                    ))  
                
                print ("{:<20} {:<10} {:<15} {:<10} {:<15} {:<20} {:<15}".format(student[0],
                                                                student[1],
                                                                student[2],
                                                                student[3],
                                                                student[4],
                                                                student[5],
                                                                student[6]
                                                                ))

                out_loop = input("Bạn muốn tùy chỉnh thêm thông tin gì nữa không: [Y]/[N]: ")
                if out_loop == "N":
                    break
                elif out_loop == "Y":
                    continue
                else:
                    out_loop = input("Bạn muốn tùy chỉnh thêm thông tin gì nữa không: [Y]/[N]")


    if not found:
        print(f"Không tìm thấy học sinh có MSSV {id_student}.")

def Show_tool(): # Hàm HIỂN THỊ danh sách thông tin của học sinh
    Apperance_tool("d")
    if not student_list_infor:
        print("Chưa có học sinh nào trong danh sách.")
        return

    # In tiêu đề
    GUI("list")

    # In từng học sinh
    for student in student_list_infor:
        print("{:<20} {:<10} {:<15} {:<10} {:<15} {:<20} {:<15}".format(student[0], 
                                                                        student[1], 
                                                                        student[2], 
                                                                        student[3],
                                                                        student[4], 
                                                                        student[5], 
                                                                        student[6]))

def Apperance_tool(text):
    if (text == "a"):
        print ("====================================================================")
        print ("Công cụ THÊM thông tin học sinh")
    elif (text == "e"):
        print ("====================================================================")
        print ("Công cụ XÓA thông tin học sinh")
    elif (text == "f"):
        print ("====================================================================")
        print ("Công cụ TÌM KIẾM thông tin học sinh")
    elif (text == "m"):
        print ("====================================================================")
        print ("Công cụ TÙY CHỈNH thông tin học sinh")
    elif (text == "d"):
        print("====================================================================")
        print("Công cụ HIỂN THỊ danh sách thông học sinh")
    else:
        return

def GUI(text):
    if (text == "form"):
        print ("====================================================================")
        print ("<<< Form điền thông tin của học sinh >>>")
        print ("[============================]")
        print ("[1. Họ và tên:               ]")
        print ("[2. MSSV:                    ]")
        print ("[3. Lớp:                     ]")
        print ("[4. Năm sinh:                ]")
        print ("[5. GVCN:                    ]")
        print ("[6. Phụ huynh:               ]")
        print ("[7. Số điện thoại:           ]")
        print ("[============================]")  
    elif (text == "list"):
        print ("{:<20} {:<10} {:<15} {:<10} {:<15} {:<20} {:<15}".format("Họ và tên [1]", 
                                                                "MSSV [2]", 
                                                                "Lớp [3]", 
                                                                "Năm sinh [4]", 
                                                                "Giáo viên [5]", 
                                                                "Phụ huynh [6]", 
                                                                "SĐT phụ huynh [7]"
                                                                )) 
    elif (text == "logo_teky"):
        word = "TEKY"
        for row in range(6):
            for letter in word:
                print(logo_all[letter][row], end="  ")
            print()

    elif (text == "logo_beniot"):
        word = "PHAN BAO TIN"
        for row in range(6):
            for letter in word:
                print(logo_all[letter][row], end="  ")
            print()
    
    else:
        print ("Không tồn tại GUI này trong hàm GUI()")

def Student_system(exit_event):
    while exit_event:
        print ("====================================================================")
        print ("Chức năng tùy chỉnh với thông tin")
        print ("- Nhập <m> để CHỈNH SỬA thông tin [1->7]")
        print ("- Nhập <e> để XÓA thông tin [1->7]")
        print ("- Nhập <f> để TÌM kiếm thông tin [1->7]")
        print ("- Nhập <a> để THÊM thông tin [1->7]")
        print ("- Nhập <d> để HIỂN THỊ thêm thông tin [1->7]")
        print ("- Nhập <exit> để THOÁT chương trình")

        tool = input("Nhập vào dụng cụ <m> <e> <f> <a> <exit> bạn muốn: ")

        if (tool == "exit"):
            print ("!!! THOÁT KHỎI hệ thống quản lí thông tin học sinh !!!")
            exit_event = False # Cờ ngắt để thoát khỏi chương trình QUẢN LÍ THÔNG TIN Học sinh
        # Tạo các hàm quản lí dữ liệu cơ bản 
        elif (tool =="a"): Add_tool()
        elif (tool =="m"): Modify_tool()
        elif (tool =="e"): Erase_tool()    
        elif (tool =="f"): Find_tool()
        elif (tool =="d"): Show_tool()
        else:
            print("!!! Cú pháp yêu cầu của bạn KHÔNG ĐÚNG theo hướng dẫn !!!")
            print("Vui lòng nhập lại theo trên")
        print("\n")

def Techer_log_in():
    print ("=== Đăng nhập hệ thống giáo viên ===")
    teacher_mail = input("Vui lòng nhập tài khoản: ")
    teacher_pass = input("Vui lòng nhập vào mật khẩu: ")
    for i in range (len(teacher_mail_list)):
        if (teacher_mail == teacher_mail_list[i] and teacher_pass == teacher_pass_list[i]):
            print ("!!! Đã đăng nhập thành công vào tài khoản !!!")
            return True
        else:
            return False

def main():
    if (Techer_log_in()):
        GUI("logo_teky")
        print("Tất cả đoạn chương trình phía dưới được thực hiện bởi: BENIOT - Phan Bảo TÍn")
        GUI("logo_beniot")
        print ("***Nhấn cú pháp - STD_INFO -> Để truy cập vào hệ thống thông tin học sinh***")
        access_syntax = input("Nhập vào cú pháp phù hợp: ")

        if (access_syntax == "STD_INFO"):
            GUI("form")
            Student_system(exit_event)
        else:
            i = 1
            while i<5: # Nhập cú pháp sai 5 lần trở lên sẽ bị KHÓA
                print("Bạn còn {} lần thử".format(5-i))
                print ("***Nhấn cú pháp - STD_INFO***")
                access_syntax = input("Nhập vào cú pháp phù hợp: ")
                if (access_syntax == "STD_INFO"):
                    print ("***Bạn đã đăng nhập thành công vào hệ thống***")
                    GUI()
                    Student_system(exit_event)
                i+=1

            print("Bạn đã hết lượt thử, vui lòng hãy tải lại trang web")
    else:
        print("!!! Thông tin tài khoản không hợp lệ. Mời quý thầy cô nhập lại !!!")

main()
