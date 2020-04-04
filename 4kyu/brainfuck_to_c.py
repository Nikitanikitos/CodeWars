CODE = {"+": "*p +=", "-": "*p -=",
        ">": "p +=", "<": "p -=",
        ".": "putchar(*p);\n",
        ",": "*p = getchar();\n",
        "[": "if (*p) do {\n",
        "]": "} while (*p);\n"}


def valid_parentheses(string):
    top = 0
    stack = ''
    for char in string:
        if char == '[':
            stack += char
            top += 1
        if char == ']':
            if top == 0: return False
            top -= 1
            if not stack[top] == '[':
                return False
    return top == 0


def refactor_code(source_code):
    while True:
        if '[]' in source_code:
            source_code = source_code[:source_code.index('[]')] + source_code[source_code.index('[]') + 2:]
        else:
            return source_code


def brainfuck_to_c(source_code):
    if valid_parentheses(source_code):
        source_code = refactor_code(source_code)
        result = ""
        space = ""
        p = 0
        flag = True
        for char in source_code:
            if char == ']':
                space = ""
            if char in "+-><" and flag:
                result += space + CODE[char]
                flag = False
            if char in '+-<>':
                p += 1
            elif flag is False and char in CODE.keys():
                result += f" {p};\n"
                p = 0
                flag = True
                result += space + CODE[char]
            elif char in CODE.keys():
                result += space + CODE[char]
            if char == '[':
                space = "  "

        if flag is False:
            result += f" {p};\n"
        return result
    else:
        return 'Error!'


print(brainfuck_to_c("++ ++"))
