TEN_NUMBER={
    90: 'ninety',
    80: 'eighty',
    70: 'seventy',
    60: 'sixty',
    50: 'fifty',
    40: 'forty',
    30: 'thirty',
    20: 'twenty'
}
UNIT_NUMBER={
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
}
def say(number):
    if number == 0:
        return 'zero'
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")
    result=""
    count=0
    if number >= 1_000_000_000:
        if number % 1_000_000_000==0:
            return say(number//1_000_000_000)+' billion'
        result=say(number//1_000_000_000)+' billion '
        number-=(number//1_000_000_000)*1_000_000_000
    if number >= 1_000_000:
        if number % 1_000_000==0:
            return say(number//1_000_000)+' million'
        result+=say(number//1_000_000)+' million '
        number-=(number//1_000_000)*1_000_000
    if number >= 1_000:
        if number % 1_000==0:
            return say(number//1_000)+' thousand'
        result+=say(number//1_000)+' thousand '
        number-=(number//1_000)*1_000
    if number >= 100:
        if number % 100==0:
            return say(number//100)+' hundred'
        result+=say(number//100)+' hundred '
        number-=(number//100)*100
    for keys, item in TEN_NUMBER.items():
        if number >= keys:
            if number % keys==0:
                result+=item
            else:
                result+=item+'-'
            number-= keys
            break
    for keys, item in UNIT_NUMBER.items():
        if number==keys:
            result+=item
    return result