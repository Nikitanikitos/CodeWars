#include <stdio.h>

typedef struct	Data {
     int 	*array;
     int 	sz;
}				Data;

int		array[6];
// array[6] = 0;
int i = 0;
int sqInRect(int lng, int wdth) {
	int		square;

	square = 0;
	while (wdth > 1 && lng > 2)
	{
		if (square >= wdth)
			square = sqInRect(wdth, lng - wdth);
		printf("%d", square);
		if (square >= lng)
			 square = sqInRect(wdth - lng, lng);
		square++;
	}
	return square;
}

int		main()
{
	sqInRect(20, 14);
}