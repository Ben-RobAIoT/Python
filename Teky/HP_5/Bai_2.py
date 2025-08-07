"""
Chức năng:
Nhập số huy chương Vàng, Bạc, Đồng cho mỗi quốc gia.

Tính tổng điểm theo quy tắc:
    Vàng = 3 điểm
    Bạc = 2 điểm
    Đồng = 1 điểm
    
Hiển thị bảng tổng kết huy chương và điểm của từng quốc gia.
"""
countries = [
    "Brunei", "Cambodia", "Indonesia", "Laos", "Malaysia",
    "Myanmar", "Philippines", "Singapore", "Thailand",
    "Timor-Leste", "Vietnam"
]

score = {}

for i in range(11):
    print("=============================")
    print("Nhập vào nước: ", countries[i])
    gold = int(input("Nhập số huy chương vàng: "))
    silver = int(input("Nhập số huy chương bạc: "))
    bronze = int(input("Nhập số huy chương đồng: "))

    score_cal = gold*3 + silver*2 + bronze
    score[i] = score_cal
    
print("=============================")

for i in range(11):
    print("Nước: ", countries[i], "đạt: ", score[i], "điểm")
