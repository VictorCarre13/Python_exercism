def prime(number):
    if number <1 :
        raise ValueError('there is no zeroth prime')
    prime_number=[]
    count=2
    while len(prime_number) < number:
        is_prime= True
        for divide in range(2,int(count**0.5)+1):
            if count % divide == 0:
                is_prime=False
                break
        if is_prime:
            prime_number.append(count)
        count+=1
    return prime_number[number-1]
