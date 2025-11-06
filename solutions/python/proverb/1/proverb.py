def proverb(*args, qualifier):
    if len(args)==0:
        return []
    if not qualifier and len(args)==1:
        return [f"And all for the want of a {args[0]}."]
    final_sentence=f"And all for the want of a {qualifier} nail."
    if len(args)==1:
        return [final_sentence]
    result=[]
    for index in range(1, len(args)):
        result.append(f"For want of a {args[index-1]} the {args[index]} was lost.")
    if not qualifier:
        result.append(f"And all for the want of a {args[0]}.")
    else:
        result.append(final_sentence)
    return result