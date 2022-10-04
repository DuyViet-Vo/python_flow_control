
import re


print("Chương trình đăng tại freetuts.net!")

print("Nhập vào số N: ")

n = int(input())
result = []

for i in range(1, n):
    if (n % i == 0 and i % 2 != 0):
        result.append(i)
print("ước lẻ lớn nhất: ", max(result))
