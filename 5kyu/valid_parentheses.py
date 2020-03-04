def valid_parentheses(string):
    top = 0
    stack = ''
    for char in string:
        if char == '(':
            stack += char
            top += 1
        if char == ')':
            if top == 0:
                return False
            top -= 1
            if not stack[top] == '(':
                return False
    if top == 0:
        return True
    else:
        return False

print(valid_parentheses("hi())("))