x = int(input("Nhap x: "))
n = int(input("Nhap n: "))
# t = x**n
t = 1
for num in range(1, n+1):
    t *= x
    print("t= {}".format(t))
print("T bang {}".format(t))