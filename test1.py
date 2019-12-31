def is_prime(num):
    '''
    Naive method of checking for primes.
    '''
    for n in range(2,num): #Ở đây chỉ lấy từ 2 và dưới số đó 1 đơn vị, ta sẽ lấy số đó chia hết cho từng số nếu ko chia hết thì
        if num % n == 0: #chứng tỏ số đó chỉ chia hết cho 1 và chính nó.
            print(num,'is not prime') #(mặc định quy luật trước khi chạy vòng for là chia hết cho chính nó và 1)
            break
    else: # If never mod zero, then prime
        print(num,'is prime!')

is_prime(2)