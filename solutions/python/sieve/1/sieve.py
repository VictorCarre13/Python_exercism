def primes(limit):
    if limit < 2:
        return []
    result=[]
    for index in range(2, limit+1):
        if is_prime(index):
            result.append(index)
    return result

def is_prime(number):
    for index in range(2, number):
        if number % index == 0:
            return False
    return True
