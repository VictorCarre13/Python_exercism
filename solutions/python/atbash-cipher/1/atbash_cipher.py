plain='abcdefghijklmnopqrstuvwxyz'
cipher='zyxwvutsrqponmlkjihgfedcba'
def encode(plain_text):
    result=""
    count=0
    for item in plain_text.lower().replace(",","").replace(' ',''):
        if item.isalpha():
            result+=cipher[plain.index(item)]
            count+=1
        elif item.isdigit():
            result+=item
            count+=1
        if count %5==0:
            result+=' '
    return result.rstrip()


def decode(ciphered_text):
    result=""
    for item in ciphered_text:
        if item.isalpha():
            result+=plain[cipher.index(item)]
        elif item.isdigit():
            result+=item
    return result