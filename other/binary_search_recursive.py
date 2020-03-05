def binary_serch(digit_list, item):
    low = 0
    high = len(digit_list) - 1

    mid = high + low
    guess = digit_list[mid]
    if guess == item:
        return mid
    if guess > item:
        high = mid
        return binary_serch(digit_list[:high], item)
    else:
        low = mid
        return binary_serch(digit_list[low:], item)

my_list = [1, 3, 5, 7, 9, 11, 13, 15, 21]
print(binary_serch(my_list, 11))