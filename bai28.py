n = int(input("Nhap n = "))
l = []
s: int = 0
for num in range(1, n+1):
    if n%num == 0 and num < n:
        l.append(num)
        s += num
print("Tong cac uoc so nho hon {} la {}, {}".format(n, s, l))