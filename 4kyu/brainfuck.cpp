#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

void    brainfuck(char *str)
{
	char	*buff;
    int		count;
	int		i;

	buff = (char*)malloc(sizeof(char) * 256);
	while(buff[i])
	{
		buff[i] = 0;
		i++;
	}
	while (*str)
	{
		if (*str == '+')
			(*buff)++;
		if (*str == '-')
			(*buff)--;
		if (*str == '>')
			buff++;
		if (*str == '<')
			buff--;
		if (*str == '.')
			write(1, &*buff, 1);
		if (*str == '[' && !*buff)
		{
			count = 1;
			while (count)
			{
				str++;
				if (*str == '[')
					count++;
				if (*str == ']')
					count--;
			}
		}
		if (*str == ']' && *buff)
		{
			count = 1;
			while (count)
			{
				str--;
				if (*str == '[')
					count--;
				if (*str == ']')
					count++;
			}
		}
		str++;
    }
}


int		main(int ac, char **av)
{
	if (ac == 2)
		brainfuck(av[1]);
	else
		write(1, "\n", 1);
	return (0);
}