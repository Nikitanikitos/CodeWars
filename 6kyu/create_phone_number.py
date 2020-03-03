# -*- coding: utf-8 -*-

def create_phone_number(n):
    res = '('
    i = 0
    while i < 3:
        res += str(n[i])
        i += 1
    res += ') '
    while i < 6:
        res += str(n[i])
        i += 1
    res += '-'
    while i < 10:
        res += str(n[i])
        i += 1
    return res
