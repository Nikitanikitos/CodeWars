def solution(string, markers):
    i = 0
    res = ''
    lengh = len(string)
    while i < lengh:
        if string[i + 1] == markers[0] or string[i + 1] == markers[1]:
            while string[i] != '\n':
                i += 1
                if i == lengh:
                    return res
            if string[i] != '\n':
                res += ' '
        res += string[i]
        i += 1
    return res