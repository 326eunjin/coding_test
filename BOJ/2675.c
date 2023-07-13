#include <stdio.h>
void str_iterate(char *str)
{
	int iterate;
	iterate=str[0]-48;
	// str++;
	printf("%s\n",str);
}
int main()
{
	int num;
	char str[30];
	scanf("%d",&num);
	for(int i=0;i<num;i++)
	{
		scanf("%s",str);
		str_iterate(str);
	}
}