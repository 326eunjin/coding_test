#include <stdio.h>
void print_star(int a)
{
	for(int i = 0;i<a;i++)
	{
		for(int j=i;j<a-1;j++)
			printf(" ");
		for(int z=0;z<=i;z++)
			printf("*");
		printf("\n");
	}
}
int main()
{
	int a;
	scanf("%d",&a);
	print_star(a);
}