s = 0
n = int(input("Nhap n = "))
if n == 0:
    print("Khong hop le, Yeu cau nhap so khac")
else:
    for num in range(1, n+1):
        s += 1/(2*num)
        print("Voi num = {} thi s = {}".format(num, s))
    print("Tong S la: {}".format(s))


