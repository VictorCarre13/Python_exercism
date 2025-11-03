def decode(string):
    result=""
    factor=""
    for item in string:
        if item.isdigit():
            factor+=item
        else:
            result+=item * int(factor or 1)
            factor=""
    return result
    
def encode(string):
    result=""
    count=1
    for index in range(0, len(string)):
        if index+1 <= len(string)-1:
            if string[index] == string[index+1]:
                count +=1
            elif count>1:
                result+=str(count)+string[index]
                count=1
            else:
                result+=string[index]
        elif count>1:
            result+=str(count)+string[index]
            count=1
        else:
            result+=string[index]
    return result
