n = int(input('Nhap n = '))
k = 2 ** (0.5)
k1 = (2 + k) ** (0.5)
if n==1 :
    print("S bang {}".format(2 ** (0.5)))
elif n==2:
    k = 2 ** (0.5)
    k1 = (2 + k) ** (0.5)
    print("S bang {}".format(k1))
else:
    for num in range(3, n+1):
        k2 = (2+k1) ** (0.5)
        k1 = k2
    print("S bang {}".format(k2))



