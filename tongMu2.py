from numpy import intp


print(" python tinhTongN.py")
n = int(input("nhập n: "))
s = 0
i = 1
while (i <= n):
    s += i**2
    i += 1
print("tổng là: ", s)
