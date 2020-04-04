def all_zero(number):
    if '0' in number:
        return len(number) - 1 == number.count('0')
    return False


def same_numbers(number):
    return len(number) == number.count(number[0])


def is_increment(number):
    return str(number) in '1234567890'


def is_decrement(number):
    return str(number) in '9876543210'


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def is_interesting(number, awesome_phrases):
    if number in awesome_phrases:
        return 2
    elif number + 1 in awesome_phrases or number + 2 in awesome_phrases:
        return 1
    occurs_1 = str(number + 2)
    occurs_2 = str(number + 1)
    number = str(number)
    if int(number) > 99:
        if all_zero(number):
            return 2
        elif same_numbers(number):
            return 2
        elif is_increment(number):
            return 2
        elif is_decrement(number):
            return 2
        elif is_palindrome(number):
            return 2
    if int(number) > 97:
        if all_zero(occurs_1) or all_zero(occurs_2):
            return 1
        elif same_numbers(occurs_1) or same_numbers(occurs_2):
            return 1
        elif is_increment(occurs_1) or is_increment(occurs_2):
            return 1
        elif is_decrement(occurs_1) or is_decrement(occurs_2):
            return 1
        elif is_palindrome(occurs_1) or is_palindrome(occurs_2):
            return 1
    return 0


print(is_interesting(99, []))
