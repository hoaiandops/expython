n = int(input("Nhap n = "))
l = []
s: int = 0
for num in range(1, n+1):
    if n%num == 0:
        l.append(num)
        s += num
        print("l = {}, s = {}".format(l,s))
print("Tong uoc so cua n la: {}".format(s))
