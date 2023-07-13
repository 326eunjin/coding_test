#include <stdio.h>
void count_each(int input,int *arr)
{
	while(input>0)
	{
		arr[input%10]++;
		input=input/10;
	}
}
int main()
{
	int first,second,third;
	scanf("%d",&first);
	scanf("%d",&second);
	scanf("%d",&third);
	int arr[10];
	for(int i=0;i<10;i++)
		arr[i]=0;
	count_each(first*second*third,arr);
	for(int i=0;i<10;i++)
		printf("%d\n",arr[i]);
}