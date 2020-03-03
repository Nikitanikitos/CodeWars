def wave(str):
    res_list = []
    for i in range(len(str)):
        new_word = str[:i] + str[i].upper() + str[i + 1:]
        if str[i] != ' ':
            res_list += [new_word]
    return res_list

print(wave("two words"))