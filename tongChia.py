print("S(n) = 1 + ½ + 1/3 + … + 1/n")
s = 1
n = int(input("nhập n: "))
i = 2
while i <= n:
    s += 1/i
    i += 1
print("tổng là : %f" % s)
