n = int(input("Nhap n = "))
l = []
for num in range(1, n+1):
    if n%num == 0 and num%2 != 0:
        l.append(num)
    else:
        continue
print("Uoc so le cua n la : {}".format(l))

# Nhap n = 60
# Uoc so cua n la : [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60]
#
# Process finished with exit code 0