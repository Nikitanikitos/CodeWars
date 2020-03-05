def recursive_sum(digit_list):
    if len(digit_list) == 1:
        return digit_list.pop()
    return digit_list.pop() + recursive_sum(digit_list)

print(recursive_sum([1, 2, 6, 9, 12, 1, 2, 60, 9, 120, 1, 2, 6, 9, 12, 1, 2, 60]))