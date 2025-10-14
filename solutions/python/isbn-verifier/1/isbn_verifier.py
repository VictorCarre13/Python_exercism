def is_valid(isbn):
    for d in isbn:
        if d.isalpha() and d.lower() !='x':
            return False
    digits=[d for d in isbn if d.isdigit() or (d.lower() == 'x' and d==isbn[-1])]
    count=0
    for index, d in enumerate(digits):
        if d.lower()=='x':
            d=10
            print(d)
        count+=int(d)*(10-index)
    return count % 11 == 0 and len(digits)==10