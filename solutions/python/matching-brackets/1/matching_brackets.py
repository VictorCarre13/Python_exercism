def is_paired(input_string):
    try:
        brackets_opens=['{','(','[',]
        brackets_closed=['}',')',']']
        searchs=[]
        for index, item in enumerate(input_string.replace(" ","")):
            if item in brackets_closed and len(searchs)==0:
                return False
            elif item in brackets_opens:
                searchs.append(brackets_closed[brackets_opens.index(item)])
            elif item not in searchs and item in brackets_closed:
                return False
            elif item==searchs[len(searchs)-1]:
                searchs.pop(len(searchs)-1)
        if len(searchs)==0:
            return True
        return False
    except IndexError:
        return True

