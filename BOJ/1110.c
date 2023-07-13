#include <stdio.h>
int get_cycle(int input)
{
	int tmp,result;
	int first,second,third;
	tmp=input;
	result=0;
	while(1)
	{
	first=tmp/10;
	second=tmp%10;
	third=first+second;
	result++;
	tmp=second*10+third%10;
	if(tmp==input)
		break;
	}
	return result;
}
int main()
{
	int input;
	scanf("%d",&input);
	printf("%d",get_cycle(input));
}