color_dict={'black':0,'brown':1,'red':2,'orange':3,
                'yellow':4,'green':5,'blue':6,
               'violet':7, 'grey':8,'white':9
               }
ohms_list=[" ohms", "0 ohms", "00 ohms",
           " kiloohms","0 kiloohms", "00 kiloohms",
           " megaohms","0 megaohms", "00 megaohms"," gigaohms"]
def label(colors):
    if color_dict[colors[0]]==0 and color_dict[colors[1]]==0:
        return ohms_list[1]
    if color_dict[colors[1]]!=0 and color_dict[colors[0]]!=0:
        return str(color_dict[colors[0]])+str(color_dict[colors[1]])+ohms_list[color_dict[colors[2]]]
    if color_dict[colors[1]]!=0:
        return str(color_dict[colors[1]])+ohms_list[color_dict[colors[2]]]
    return str(color_dict[colors[0]])+ohms_list[color_dict[colors[2]]+1]