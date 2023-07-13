#include <stdio.h>
void first_second(int *arr)
{
	for (int i = 1; i < 100; i++)
		arr[i]++;
}
void three_digits(int *arr)
{
	int first;
	int second;
	int third;
	for (int i = 100; i < 1000; i++)
	{
		first = i / 100;
		second = (i % 100) / 10;
		third = (i % 100) % 10;
		if (second - first == third - second)
			arr[i]++;
	}
}
void four_digits(int *arr)
{
	int first;
	int second;
	int third;
	int fourth;
	for (int i = 1000; i < 10000; i++)
	{
		first = i / 1000;
		second = (i % 1000) / 100;
		third = (i % 100) / 10;
		fourth = (i % 10);
		if ((second - first == third - second) && (third - second == fourth - third))
			arr[i]++;
	}
}
int ret_num(int *arr, int input)
{
	int tmp = 0;
	for (int i = 1; i <= input; i++)
		if (arr[i] != 0)
			tmp++;
	return tmp;
}
int main()
{
	int arr[10000];
	int input;
	scanf("%d", &input);
	first_second(arr);
	three_digits(arr);
	four_digits(arr);
	printf("%d", ret_num(arr, input));
}