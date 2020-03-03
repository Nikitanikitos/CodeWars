# -*- coding: utf-8 -*-

def is_square(n):
    mul = 0
    if n < 0:
        print("{}: Negative numbers cannot be square numbers".format(n))
        return False
    while mul * mul <= n:
        if mul * mul == n:
            print("{}: is a square number".format(n))
            return True
        mul += 1
    print("{}: is a not square number".format(n))
    return False
