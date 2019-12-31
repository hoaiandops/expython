x = int(input("Nhap x = "))
n = int(input("Nhap n = "))
k = 2*n
m = 1
s: int = 1
m1: int = 1
for num in range(1, k+1):
    m1 *= num
    m *= x
    if num%2 == 0:
        h = m/m1
        s += h
    else:
        continue
    print("m = {}, m1= {}, h= {}, s= {}".format(m, m1, h, s))
print("Tong s bang {}".format(s))

