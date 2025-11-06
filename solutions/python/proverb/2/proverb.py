def proverb(*args, qualifier):
    if not args:
        return []
    if not qualifier and len(args)==1:
        return [f"And all for the want of a {args[0]}."]
    final_sentence=f"And all for the want of a {qualifier} nail."
    if len(args)==1:
        return [final_sentence]
    result=[]
    for index in range(1, len(args)):
        result.append(f"For want of a {args[index-1]} the {args[index]} was lost.")
    result.append(f"And all for the want of a {args[0]}." if not qualifier else final_sentence)
    return result