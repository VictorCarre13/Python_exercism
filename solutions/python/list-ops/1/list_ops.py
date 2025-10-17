def append(list1, list2):
    result=[]
    for x in list1:
        result+=[x]
    for x in list2:
        result+=[x]
    return result

def concat(lists):
    result=[]
    for sublist in lists:
        for item in sublist:
            result+=[item]
    return result


def filter(function, list):
    result=[]
    for item in list:
        if function(item):
            result+=[item]
    return result


def length(list):
    count=0
    for _ in list:
        count+=1
    return count


def map(function, list):
    return [function(item) for item in list]


def foldl(function, list, initial):
    for item in list:
        initial=function(initial,item)
    return initial


def foldr(function, list, initial):
    for item in reverse(list):
        initial=function(initial,item)
    return initial


def reverse(list):
    result=[]
    for index in range(0,length(list)):
        result+=[list[-(index+1)]]
    return result
