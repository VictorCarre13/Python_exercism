import re
class PhoneNumber:
    def __init__(self, number):
        self.number, self.area_code= Clean(number)
        
    def pretty(self):
        return f"({self.area_code})-{self.number[3:6]}-{self.number[6:]}"
        
def Clean(number):
    #Test when area code is obvious
    area_code=re.search(r'\((\d+)\)', number)
    if area_code:
        area_code=area_code.group(1)
        if area_code.startswith('1'):
            raise ValueError("area code cannot start with one")
        if area_code.startswith('0'):
            raise ValueError("area code cannot start with zero")   
    number=re.sub(r"[+ ()-.]", '', number)
    
    #Raise error if letters or punctations
    for item in number:
        if item.isalpha():
            raise ValueError("letters not permitted")
        elif not item.isdigit():
            raise ValueError("punctuations not permitted")

    #Erase 1 if exist
    numero=number
    if number.startswith('1'):
        numero=number[1:]
        
    #Test for area_code
    if not area_code:
        area_code=numero[:3]
        if area_code.startswith('1'):
            raise ValueError("area code cannot start with one")
        if area_code.startswith('0'):
            raise ValueError("area code cannot start with zero")
    
    #Test for exchange
    exchange=numero[3]
    if exchange.startswith('1'):
        raise ValueError("exchange code cannot start with one")
    if exchange.startswith('0'):
        raise ValueError("exchange code cannot start with zero")
        
    #Len test
    if len(numero) < 10:
        raise ValueError("must not be fewer than 10 digits")
    if len(numero) > 11:
        raise ValueError("must not be greater than 11 digits")
    if len(numero)==11 and number[0]!='1':
        raise ValueError("11 digits must start with 1")
        
    return numero, area_code