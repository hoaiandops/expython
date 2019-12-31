n = int(input("Nhap n = "))
l = []
s: int = 0
for num in range(1, n+1):
    if n%num == 0 and num%2 == 0:
        l.append(num)
        s += num
    else:
        continue
print("Tong Uoc so chan cua n la : {} {}".format(s, l))
