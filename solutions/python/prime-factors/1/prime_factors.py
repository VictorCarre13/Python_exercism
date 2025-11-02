def factors(value):
    if value <1:
        return []
    factors=[]
    factor=2
    while value >1:
        if value % factor == 0:
            value //= factor
            factors.append(factor)
        else:
            factor+=1
    return factors