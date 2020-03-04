def fibonacci(n):
    i = 0
    prev = 0
    next = 1
    res = 0
    while i < n - 1:
        res = next + prev
        prev = next
        next = res
        i += 1
    return res


print(fibonacci(70))
