n = int(input('nhâp n: '))
if n <= 2:
    print("số %i là số nguyên tố" % n)
v = True
for i in range(2, n):
    if (n % i == 0):
        v = False

if (v == True):
    print("số %i là số nguyên tố" % n)
else:
    print("số %i không số nguyên tố" % n)
