import math, time


def proper_fractions(n):
    if n == 0: return 0
    res = 1
    dec_list = []
    for i in range(2, n):
        if n % i == 0:
            dec_list.append(i)
            continue
        for q in dec_list:
            if n % q == 0 and i % q == 0:
                break
        else:
            res += 1
    return res


def proper_fractions1(n):
    if n == 0: return 0
    res = 1
    for i in range(2, n):
        if n % i == 0:
            continue
        for q in range(2, round(math.sqrt(i)) + 1):
            if n % q == 0 and i % q == 0:
                break
        else:
            res += 1
    return res

started_at = time.time()
print(proper_fractions(1251233))
ended_at = time.time()
elapsed = round(ended_at - started_at, 4)
print(f'Функция работала {elapsed} секунд(ы)')