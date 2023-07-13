#include <stdio.h>
void one_digits(int *arr)
{
	for(int i=1;i<10;i++)
		arr[i+i]++;
}
void two_digits(int *arr)
{
	int first;
	int second;
	for(int i=10;i<100;i++)
	{
		first=i/10;
		second=i%10;
		arr[i+first+second]++;
	}
}
void three_digits(int *arr)
{
	int first;
	int second;
	int third;
	for(int i=100;i<1000;i++)
	{
		first=i/100;
		second=(i%100)/10;
		third=(i%100)%10;
		arr[i+first+second+third]++;
	}
}
void four_digits(int *arr)
{
	int first;
	int second;
	int third;
	int four;
	for(int i=1000;i<10000;i++)
	{
		first=i/1000;
		second=(i%1000)/100;
		third=(i%100)/10;
		four=(i%10);
		arr[i+first+second+third+four]++;
	}
}
void print_digits(int *arr)
{
	for(int i=1;i<10000;i++)
		if(arr[i]==0)
			printf("%d\n",i);
}
int main()
{
	int arr[10050]={0,};
	one_digits(arr);
	two_digits(arr);
	three_digits(arr);
	four_digits(arr);
	print_digits(arr);
}