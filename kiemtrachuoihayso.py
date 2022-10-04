print("Chương trình đăng tại freetuts.net")
user_input = input("Nhập tuổi của bạn ")

print("\n")
try:
    val = int(user_input)
    print("Dữ liệu nhập vào là int = ", val)
except ValueError:
    try:
        val = float(user_input)
        print("Dữ liệu nhâp vào là float = ", val)
    except ValueError:
        print("Dữ liệu nhập vào không phải là number")
