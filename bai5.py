s = 0
n = int(input("Nhap n = "))
# if n == 0:
#     print ('Tong s la 1')
# else:
for num in range(0, n+1):
    s += 1/(2*num+1)
    print("Voi num = {} thi s = {}".format(num, s))
print("Tong s la: {}".format(s))