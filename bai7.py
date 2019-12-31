s = 0
n = int(input("Nhap n = "))
for num in range(0, n+1):
    i = num/(num+1)
    s += num/(num+1)
    print("Voi num = {} thi i = {}".format(num, i))
print("Tong S la {}".format(s))