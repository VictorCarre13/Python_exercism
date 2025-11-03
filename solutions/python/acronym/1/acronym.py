def abbreviate(words):
    words = words.replace("-", " ").replace("'","").title()
    return "".join([item for item in words if item.isupper()])
    
