n = int(input("Nhap n = "))
l = []
t: int = 1
for num in range(1, n+1):
    if n%num == 0:
        l.append(num)
        t *= num
        print("l = {}, t = {}".format(l, t))
print("tich uoc so cua n la: {}".format(t))
