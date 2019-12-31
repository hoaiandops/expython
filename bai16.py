x = int(input("Nhap x = "))
n = int(input("Nhap n = "))
i = 1
k = 0
s = 0
for num in range(1, n+1):
    i *= x
    k += num
    s += i/k
    print("i = {} k = {} s = {}".format(i, k, s))
print("Tong s = {}".format(s))
