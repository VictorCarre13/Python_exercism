def flatten(iterable):
    result=[]
    while iterable:
        item=iterable.pop(0)
        if isinstance(item,list):
            iterable=item+iterable
        elif item!= None:
            result.append(item)
    return result