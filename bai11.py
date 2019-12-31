# s = 0
# t = 1
# n = int(input("Nhap n = "))
# for num in range(1,n+1):
#     t *= num
#     s += t
#     print("t = {}, s = {}".format(t,s))
# print("S bang {}".format(s))

s = 0
n = int(input("Nhap n = "))
for num in range(1, n+1):
    t = 1
    for i in range(1, num+1): #ở đây ta dùng i
        t *= i
    s += t
    print("t = {}, s = {}".format(t, s))
print("S bang {}".format(s))
