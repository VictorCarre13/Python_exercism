ROMAN_LETTER={
    1:'I',
    4:'IV',
    5:'V',
    9:'IX',
    10:'X',
    40:'XL',
    50:'L',
    90:'XC',
    100:'C',
    400:'CD',
    500:'D',
    900:'CM',
    1000:'M'
}
def roman(number):
    result=""
    for value in sorted(ROMAN_LETTER.keys(), reverse=True):
        count,number=divmod(number, value)
        result+=count*ROMAN_LETTER[value]
    return result    
