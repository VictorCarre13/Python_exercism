def egg_count(display_value):
    if display_value==0:
        return 0
    binary=[]
    while True:
        n=0
        while display_value > 2**n:
            n+=1
        if display_value==2**n:
            binary.append(1)
            break
        else:
            binary.append(1)
            display_value= display_value - 2**(n-1)
    return binary.count(1)
