SENTENCE={
    10:"Ten green bottles hanging on the wall,",
    9:"Nine green bottles hanging on the wall,",
    8:"Eight green bottles hanging on the wall,",
    7:"Seven green bottles hanging on the wall,",
    6:"Six green bottles hanging on the wall,",
    5:"Five green bottles hanging on the wall,",
    4:"Four green bottles hanging on the wall,",
    3:"Three green bottles hanging on the wall,",
    2:"Two green bottles hanging on the wall,",
    1:"One green bottle hanging on the wall,",
    0:"And if one green bottle should accidentally fall,",
}
final_word={
    10:"nine",
    9:"eight",
    8:"seven",
    7:"six",
    6:"five",
    5:"four",
    4:"three",
    3:"two",
    2:"one",
    1:"no"
}
def recite(start, take=1):
    result=[]
    for index in range(take):
        result.append(SENTENCE[start])
        result.append(SENTENCE[start])
        result.append(SENTENCE[0])
        if start!=2:
            result.append(f"There'll be {final_word[start]} green bottles hanging on the wall.")
        else:
            result.append(f"There'll be {final_word[start]} green bottle hanging on the wall.")
        start-=1
        if index < take-1:
            result.append("")
    return result
