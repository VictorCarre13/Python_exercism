VERSE={
    1:"This is the house that Jack built.",
    2:" that lay in the house that Jack built.",
    3:" that ate the malt",
    4:" that killed the rat",
    5:" that worried the cat",
    6:" that tossed the dog",
    7:" that milked the cow with the crumpled horn",
    8:" that kissed the maiden all forlorn",
    9:" that married the man all tattered and torn",
    10:" that woke the priest all shaven and shorn",
    11:" that kept the rooster that crowed in the morn",
    12:" that belonged to the farmer sowing his corn"
}
PRODUCTS={
    2:"malt",
    3:"rat",
    4:"cat",
    5:"dog",
    6:"cow with the crumpled horn",
    7:"maiden all forlorn",
    8:"man all tattered and torn",
    9:"priest all shaven and shorn",
    10:"rooster that crowed in the morn",
    11:"farmer sowing his corn",
    12:"horse and the hound and the horn"
}
def recite(start_verse, end_verse):
    result=[]
    index=start_verse
    for number in range(start_verse, end_verse+1):
        result.append(verse(number))  
    return result
    
def verse(number):
    if number==1:
            return VERSE[1]
    verse=f"This is the {PRODUCTS[number]}"
    for index in reversed(range(1,number)):
        verse=verse+VERSE[number]
        number-=1
    return verse
