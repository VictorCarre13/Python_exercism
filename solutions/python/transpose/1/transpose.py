def transpose(text):
    text = text.split('\n')
    result={}
    max=0
    for item in text:
        if len(item)>max:
            max=len(item)
    for item in text:
        count = len(item)
        for index in range(0, count):
            caracter=item[index]
            if caracter==' ':
                caracter='_'
            if index in result:
                result[index]+=caracter
            else:
                result[index]=caracter
        for index in range(count, max):
            if index in result:
                result[index]+=' '
            else:
                result[index]=' '
    value=""
    for item in result.values():
        value+=f'{item.rstrip()}\n'
    value=value.replace('_', ' ').rstrip('\n')
    return value