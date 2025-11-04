SONG_OBJECT= {
    1:'a Partridge in a Pear Tree.',
    2:'two Turtle Doves, ',
    3:'three French Hens, ',
    4:'four Calling Birds, ',
    5:'five Gold Rings, ',
    6:'six Geese-a-Laying, ',
    7:'seven Swans-a-Swimming, ',
    8:'eight Maids-a-Milking, ',
    9:'nine Ladies Dancing, ',
    10:'ten Lords-a-Leaping, ',
    11:'eleven Pipers Piping, ',
    12:'twelve Drummers Drumming, '
}
ORDINAL_NUMBER={
    1:'first',
    2:'second',
    3:'third',
    4:'fourth',
    5:'fifth',
    6:'sixth',
    7:'seventh',
    8:'eighth',
    9:'ninth',
    10:'tenth',
    11:'eleventh',
    12:'twelfth'
}
def recite(start_verse, end_verse):
    result=[]
    if start_verse != end_verse:
        for index in range(start_verse, end_verse+1):
            result.extend(recite(index, index))
        return result
    else:
        first_verse=f"On the {ORDINAL_NUMBER[start_verse]} day of Christmas my true love gave to me: "
        for index in range(start_verse, 0, -1):
            if index==1 and start_verse > 1:
                first_verse+='and '
            first_verse+=SONG_OBJECT[index]
        return [first_verse]