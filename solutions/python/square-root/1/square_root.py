def square_root(number):
    for i in range(1, number+1):
        if number % i == 0 and i*i==number:
            return i
    