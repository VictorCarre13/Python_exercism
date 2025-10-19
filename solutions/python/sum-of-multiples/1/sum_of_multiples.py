def sum_of_multiples(limit, multiples):
    if limit < 1:
        raise ValueError("Level doesn't exist")
    result=[]
    for item in multiples:
        if item!=0:
            for index in range(1,limit):
                if index%item==0 and not index in result:
                    result.append(index)
    return sum(result)