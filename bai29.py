n = int(input("Nhap n = "))
l = []

for num in range(1, n+1):
    if n%num == 0 and num%2 != 0:
        l.append(num)
print('Uoc le lon nhat cua {} la: {} {}'.format(n, max(l), l))
#or
print('Uoc le lon nhat cua {} la: {} {}'.format(n, l[-1], l))