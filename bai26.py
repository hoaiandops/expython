n = int(input("Nhap n = "))
l = []
t: int = 1
for num in range(1, n+1):
    if n%num == 0 and num%2 != 0:
        l.append(num)
        t *= num
    else:
        continue
print("Tich Uoc so le cua n la : {} {}".format(t, l))
