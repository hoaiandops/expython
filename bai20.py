n = int(input("Nhap n = "))
l = []
for num in range(1, n+1):
    if n%num == 0:
        l.append(num)
    else:
        continue
print("Uoc so cua n la : {}".format(l))