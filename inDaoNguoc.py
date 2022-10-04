# Lấy dữ liệu
n = int(input())
so_dao_nguoc = ""
 
# B1: Đảo ngược số cần in ra
while (n != 0):
    so_dao_nguoc += str(n % 10)
    n = n // 10  # Chia lấy phần nguyên
 
# B2: In lần lượt các ký tự từ cuối đến đầu của số đã đảo
so_dao_nguoc = int(so_dao_nguoc, 10) # Đổi string sang int
 
while (so_dao_nguoc != 0):
    print(so_dao_nguoc % 10, end= ' - ')
    so_dao_nguoc = so_dao_nguoc // 10  # Chia lấy phần nguyên