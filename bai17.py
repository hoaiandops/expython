x = int(input("Nhap x = "))
n = int(input("Nhap n = "))
i = 1
k = 1
for num in range(1, n+1):
    i *= x
    k *= num
    s = i/k
print("Tong S la = {}".format(s))
