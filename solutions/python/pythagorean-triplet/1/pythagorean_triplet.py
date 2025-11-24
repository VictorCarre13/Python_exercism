def triplets_with_sum(number):
    list_possibility = []
    for a in range(1, number//3 + 1):
        for b in range(a + 1, (number - a) // 2 + 1):
            c = number - a - b
            if c > b:
                if a*a + b*b == c*c:
                    list_possibility.append([a, b, c])
            else:
                break
    return list_possibility
