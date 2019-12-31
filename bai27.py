n = int(input("Nhap n = "))
l = []

for num in range(1, n+1):
    if n % num == 0 and num % 2 == 0:
        l.append(num)
        print (l)
print(f'Co {len(l)} uoc so chung chan cua {n}')
