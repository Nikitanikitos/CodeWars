def rot13(message):
    res = ''
    for i in message:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            i = ord(i) - ord('a')
            i += 13
            i %= 26
            i += ord('a')
            res += chr(i)
        elif ord(i) >= ord('A') and ord(i) <= ord('Z'):
            i = ord(i) - ord('A')
            i += 13
            i %= 26
            i += ord('A')
            res += chr(i)
        else:
            res += i
    return res



print(rot13("Test!!!!"))
