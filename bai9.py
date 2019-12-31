# t = 1
# n = int(input("Nhap n = "))
# for num in range(1, n+1):
#     t *= num
# print("T la {}".format(t))

while True:
    t = 1
    n = int(input("Nhap n = "))
    for num in range(1, n + 1):
        t *= num
    print("T la {}".format(t))
    tieptuc = input("ban co muon tiep tuc (Y/N) ")
    if tieptuc=="Y":
        continue
    else:
        print("cam on")
        break





