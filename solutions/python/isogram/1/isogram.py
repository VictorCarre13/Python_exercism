def is_isogram(string):
    list=(string.lower()).strip()
    for item in list:
        if list.count(item) > 1 and item.isalpha():
            return False
    return True
