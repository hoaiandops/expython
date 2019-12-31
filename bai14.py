x = int(input("Nhap x = "))
n = int(input("Nhap n = "))
s = 0
i = 1
k = 2*n + 1
for num in range(1, k+1):
    i *= x
    if num % 2 == 0:
        continue
    else:
        s += i
    print("s = {} va i = {}".format(s, i))
print("Tong s = {}".format(s))
