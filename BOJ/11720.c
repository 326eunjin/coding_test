#include <stdio.h>
int main()
{
	int input;
	scanf("%d", &input);
	char str[input];
	int ret = 0;
	scanf("%s", str);
	for (int i = 0; i < input; i++)
	{
		ret = ret + str[i] - 48;
	}
	printf("%d", ret);
}