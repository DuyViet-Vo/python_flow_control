n = int(input('nhập số N: '))
s = 0
for i in range(1, n):
    if (n % i == 0):
        s += i

if (s == n):
    print('số %i đã cho là số hoàn hảo' % n)
else:
    print('số %i đã cho không phải là số hoàn hảo' % n)
