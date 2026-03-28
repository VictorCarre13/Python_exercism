def rotate(text, key):
    Plain="abcdefghijklmnopqrstuvwxyz"
    new_word=""
    if 0<= key < 13:
        for index, item in enumerate(text):
            if item.isupper():
                new_word = new_word + Plain[Plain.index(item.lower())+key].upper()
            elif item.isalpha():
                new_word = new_word + Plain[Plain.index(item)+key]
            else:
                new_word=new_word+item
    elif 13== key :
        for index, item in enumerate(text):
            if item.isupper():
                new_word = new_word + Plain[Plain.index(item.lower())-key].upper()
            elif item.isalpha():
                new_word = new_word + Plain[Plain.index(item)-key]
            else:
                new_word=new_word+item
    elif 13 < key < 26 :
        key=26-key
        for index, item in enumerate(text):
            if item.isupper():
                new_word = new_word + Plain[Plain.index(item.lower())-key].upper()
            elif item.isalpha():
                new_word = new_word + Plain[Plain.index(item)-key]
            else:
                new_word=new_word+item
    elif key == 26:
        return text
    else:
        raise ValueError("The key as to be between 0 and 26")
    return new_word
