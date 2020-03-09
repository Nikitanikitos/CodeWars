def to_postfix(infix):
    operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '(': 0}
    postfix = []
    stack = []
    for ch in infix:
        if ch.isnumeric():
            postfix.append(ch)
        elif ch in '(':
            stack.append(ch)
        elif ch in ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and operators[stack[-1]] >= operators[ch]:
                postfix.append(stack.pop())
            stack.append(ch)
    while stack:
        postfix.append(stack.pop())
    return ''.join(postfix)

print(to_postfix("5+(6-2)*9+3^(7-1)"))
