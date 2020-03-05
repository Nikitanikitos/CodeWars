# -*- coding: utf-8 -*-

def delete_nth(order, max_e):
    res = []
    for digit in order:
        if res.count(digit) < max_e:
            res.append(digit)
    return res


delete_nth([1, 1, 1, 1], 2)
