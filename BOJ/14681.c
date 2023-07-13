#include <stdio.h>
int quadrant(int a,int b)
{
	if(a>0&&b>0)//both positive
		return 1;
	else if (a>0)
		return 4;
	else if (b>0)
		return 2;
	else 
		return 3;

}
int main()
{
	int a,b;
	scanf("%d",&a);
	scanf("%d",&b);
	printf("%d",quadrant(a,b));
}