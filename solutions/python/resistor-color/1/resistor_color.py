color_dict={'black':0,'brown':1,'red':2,'orange':3,
                'yellow':4,'green':5,'blue':6,
               'violet':7, 'grey':8,'white':9
               }
def color_code(color):
    if color in color_dict:
        return color_dict[color]
    raise ValueError(f"{color}, isn't corresponding")

def colors():
    return list(color_dict)
