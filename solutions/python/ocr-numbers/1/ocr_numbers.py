OCR={
    (' _ ', '| |', '|_|', '   '):'0',
    ("   ", "  |", "  |", "   "):'1',
    (" _ ", " _|", "|_ ", "   "):'2',
    (" _ ", " _|", " _|", "   "):'3',
    ("   ", "|_|", "  |", "   "):'4',
    (" _ ", "|_ ", " _|", "   "):'5',
    (" _ ", "|_ ", "|_|", "   "):'6',
    (" _ ", "  |", "  |", "   "):'7',
    (" _ ", "|_|", "|_|", "   "):'8',
    (" _ ", "|_|", " _|", "   "):'9'
}
def convert(input_grid):
    if len(input_grid)%4 !=0:
        raise ValueError("Number of input lines is not a multiple of four")
    if any(len(item) % 3 != 0 for item in input_grid):
        raise ValueError("Number of input columns is not a multiple of three")
    group=[]
    cut=[]
    result=''
    for four in range(0, len(input_grid), 4):
        group = input_grid[four:four+4]
        if four != 0 :
            result+=','
        for three in range(0, len(group[0]), 3):
            for index in range(0, 4):
                cut.append(group[index][three:three+3])
            if tuple(cut) in OCR.keys():
                result+=OCR[tuple(cut)]
            else:
                result+='?'
            cut=[]
    return result

