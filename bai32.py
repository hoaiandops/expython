n = int(input("Nhap n = "))

for num in range(1, n+1):
    if num*num == n:
        print("{} la so chinh phuong".format(n))
        break
    elif num == n:
        print("{} khong phai la so chinh phuong".format(n))
        break
