def rgb(r, g, b):
    nbr = [r, g, b]
    res = []
    for i in nbr:
        if i < 0: i = 0
        if i > 255: i = 255
        res += [hex(i).upper().replace("0X", "")]
    r, g, b = res
    return f'{r:0>2}{g:0>2}{b:0>2}'

print(rgb(-2, 256, 125))
