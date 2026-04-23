plain='abcdefghijklmnopqrstuvwxyz'
def rows(letter):
    letters=[]
    num=plain.index(letter.lower())
    marge_a=num*2
    result=""
    count=1
    marge=0
    for item in plain[0:num+1]:
        if item == 'a': 
            letters.append(item.upper().center(marge_a+1))
        else:
            result=(f"{item.upper()}{' '*count}{item.upper()}")
            count+=2
            if len(letters[0])!=len(result):
                marge=(len(letters[0])-len(result))//2
                result=f"{' '*marge}{result}{' '*marge}"
            letters.append(result)
    letters.extend(list(reversed(letters[:-1])))
    return letters
