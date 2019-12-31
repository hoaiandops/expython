n = int(input("Nhap n = "))
s = 0
i = 1
k = 0
for num in range(1, n+1):
    k += num
    i = 1/k
    s += i
    print("k = {}, i= {}, s= {}".format(k, i, s))
print("Tong s bang {}".format(s))

# n = int(input("Nhap n = "))
# s = 0
# for num in range(1, n+1):
#     k = 0
#     for num1 in range(1, num+1):
#         k += num1
#         i = 1/k
#         print("k = {}, i= {}".format(k, i))
#     s += i
#     print("s= {}".format(s))
# print("Tong s bang {}".format(s))
