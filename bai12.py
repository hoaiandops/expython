# x = int(input('Nhap x = '))
# n = int(input('Nhap n = '))
# s = 0
# t = 1
# for num in range(1, n+1):
#     t *= x
#     s += t
# print('S = {} va t = {}'.format(s, t))

x = int(input('Nhap x = '))
n = int(input('Nhap n = '))
s = 0
for num in range(1, n+1):
    t = 1
    for num1 in range(1, num+1): #ở đây ta chỉ lấy số lần lặp
        t *= x
    s += t
print('S = {} va i = {}'.format(s, t))
