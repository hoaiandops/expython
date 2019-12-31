x = int(input("Nhap x = "))
n = int(input("Nhap n = "))
s = 0
k = 2*n
for num in range(1, k+1):
    i = 1
    for num1 in range(1, num+1):
        i *= x
    if num%2 == 0:
        s += i
    else:
        continue
print("Tong s la {}".format(s))
