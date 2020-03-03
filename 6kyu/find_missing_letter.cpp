#include <stdio.h>

char findMissingLetter(char array[], int arrayLength)
{
	for (int i = 0; i < arrayLength; i++) {
		if (array[i + 1] - array[i] != 1)
			return array[i] + 1;
	}
	return 0;
}

int		main()
{
	char	s;
	char arr1[] = {'j', 'k', 'l', 'm', 'n', 'o', 'p', 'e'};
	s =  findMissingLetter(arr1, 8);
	printf("%c", s);

}