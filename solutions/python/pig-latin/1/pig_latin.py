def translate(text):
    list_word=[]
    for item in text.split():
        list_word.append(translate_word(item))
    return " ".join(list_word)
def translate_word(text):
    if text[0] in ['a','e','i','o','u'] or text.startswith("xr") or text.startswith("yt"):
        return text+"ay"
    if text[0:2]=="qu":
        return text[2:]+text[0:2]+"ay"
    if text[1:3]=="qu":
        return text[3:]+text[0:3]+"ay"
    new_text=text
    for index, item in enumerate(text):
        if item=='y' and index==0:
            return text[1:]+'yay'
        if item=='y':
            return text[index:]+text[:index]+'ay'
        if item in ['a','e','i','o','u']:
            return new_text+"ay"
        new_text=new_text[1:]+text[index]
   
    