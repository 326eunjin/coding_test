#include <stdio.h>
int main()
{
	int a, b;
	int ret;
	while (1)
	{
		ret = scanf("%d %d", &a, &b);
		if (ret == EOF)
			break;
		printf("%d", a + b);		
	}
}