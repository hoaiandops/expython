s = 0
n =int(input('nhap n = '))
for num in range(1, n +1):
    s += 1/num
    print ("Voi num = {} thi s = {}".format(num,s))
print("S tong la: {}".format(s))