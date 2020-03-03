#include <stdbool.h>
#include <stdio.h>

bool IsIsogram(char *str) 
{
	int		i = 0;

	while(str[i])
	{
		if (str[i] >= 'A' && str[i] <= 'Z')
			str[i] += 32;
		i++;
	}
	for (int i = 0; str[i]; i++) {
		for (int j = i + 1; str[j]; j++) {
			if (str[i] == str[j] || str[i] == str[j] + 32)
				return false;
		}
	}
	return true;
}

int		main()
{
	char	str[] = "mOse"; 
	printf("%d", IsIsogram(str));
}