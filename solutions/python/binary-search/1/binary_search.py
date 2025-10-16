def find(search_list, value):
    if  not value in search_list:
        raise ValueError("value not in array")
    count=0
    while True:
        middle=len(search_list)//2
        if search_list[middle]==value:
            return middle+count
        elif search_list[middle] < value:
            search_list=search_list[middle: ]
            count+=middle
        elif search_list[middle] > value:
            search_list=search_list[:middle]