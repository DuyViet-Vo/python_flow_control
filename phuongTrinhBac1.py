# Nhập số a và kiểm tra điều kiện khác 0
print("Nhập vào số a: ")
a = int(input())
 
while True:
    if a == 0:
        print("Vui lòng nhập số a khác 0: ")
        a = int(input())
    else:
        break
 
# Nhập số b
print("Nhập vào số b: ")
b = int(input())
 
# Nghiệm
print("Nghiệm của phương trình là x = ", (-b / a))