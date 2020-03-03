def tribonacci(signature, n):
    if n <= len(signature):
        arr = signature[:n]
        return arr
    x, y, z = signature[0], signature[1], signature[2]
    i = 3
    while i < n:
        res = x + y + z
        signature.append(res)
        x, y, z = y, z, res
        i += 1
    return signature


print(tribonacci([1, 1, 1], 10))
