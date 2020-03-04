#include <stdbool.h>
#include <stdio.h>

bool validParentheses(const char* strin) {
	char	stack[50];
	int		top = 0;

	for (int i = 0; strin[i]; i++) {
		if (strin[i] == '(') {
			stack[top] = strin[i];
			top++;
		}
		if (strin[i] == ')') {
			if (top == 0)
				return false;
			top--;
			if (stack[top] != '(')
				return false;
		}
	}
	if (top != 0)
		return false;
	return true;
}

int		main()
{
	printf("%d", validParentheses("hi())("));
}