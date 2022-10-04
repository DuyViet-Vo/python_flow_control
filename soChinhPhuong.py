n = int(input('nhâp N: '))
check = False
for i in range(1,n):
    if(i**2==n):
        check = True
        break

if check == True:
    print ('số %i là số chính phương'%n)
else:
    print('số %i không là số chính phương'%n)