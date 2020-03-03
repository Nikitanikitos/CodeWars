# -*- coding: utf-8 -*-

def solution(number):
    if number == 0:
        return 0
    res = 0
    number -= 1
    while number:
        if number % 3 == 0 or number % 5 == 0:
            res += number
        number -= 1
    return res
