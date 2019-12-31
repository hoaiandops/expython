n = int(input("Nhap n = "))
l = []

for num in range(1, n+1):
    if n%num == 0:
        l.append(num)
if len(l)==2:
    print('{} la so nguyen to'.format(n))
else:
    print('{} khong phai la so nguyen to'.format(n))
