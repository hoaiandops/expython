x = int(input("Nhap x = "))
n = int(input("Nhap n = "))
k = 2*n+1
s = 1
m = 1
m1 = 1
for num in range(1, k+1):
    m *= x
    m1 *= num
    if num%2 == 0:
        continue
    else:
        h = m/m1
        s += h
    print("m = {}, m1= {}, h= {}, s= {}".format(m, m1, h, s))
print("Tong s bang {}".format(s))
