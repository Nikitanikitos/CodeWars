# -*- coding: utf-8 -*-

def in_array(array1, array2):
    r = []
    for string in array1:
        for string2 in array2:
            if string in string2 and string not in r:
                r.append(string)
    r = sorted(r)
    return r
