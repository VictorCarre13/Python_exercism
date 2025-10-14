color_dict = {'black':0,'brown':1,'red':2,'orange':3,
              'yellow':4,'green':5,'blue':6,
              'violet':7, 'grey':8,'white':9}
tolerance_dict={'grey':'±0.05%', 'violet' : '±0.1%', 'blue': '±0.25%', 
                'green': '±0.5%', 'brown': '±1%', 'red': '±2%', 
                'gold': '±5%', 'silver': '±10%'}
def resistor_label(colors):
    if len(colors)==5:
        value_1, value_2, value_3, Multiplier, Tolerance=[color_dict[c] for c in colors]
        value=(value_1*100+value_2*10+value_3)*(10**Multiplier)
    elif len(colors)==4:
        value_1, value_2, Multiplier,Tolerance=[color_dict[c] for c in colors]
        value=(value_1*10+value_2)*(10**Multiplier)
    else:
        return "0 ohms"
    Tolerance=tolerance_dict[colors[-1]]
    print(value)
    prefix=""
    if value>=1_000_000_000:
        if value % 1_000_000_000==0:
            value= value // 1_000_000_000
        else:
            value= value / 1_000_000_000
        prefix="giga"
    if value >= 1_000_000:
        if value % 1_000_000==0:
            value= value // 1_000_000
        else:
            value= value / 1_000_000
        prefix="mega"
    if value >= 1_000:
        if value % 1_000==0:
            value= value // 1_000
        else:
            value= value / 1_000
        prefix="kilo"
    return f"{value} {prefix}ohms {Tolerance}"
    