def score(dice):
    dict_res = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    res = 0
    for i in dice:
        if dice.count(i) >= 3 and i != 1:
            dict_res[i] = i * 100
        elif dice.count(i) == 3 and i == 1:
            dict_res[i] = i * 1000
        elif dice.count(i) == 4:
            if i == 5: dict_res[i] = 550
            elif i == 1: dict_res[i] = 1100
        elif i == 5:
            dict_res[i] += 50
        elif i == 1:
            dict_res[i] += 100
    for key, value in dict_res.items():
        res += value
    return res



print(score([3, 3, 3, 3, 3]))