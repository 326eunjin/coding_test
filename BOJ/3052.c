#include <stdio.h>
int compare_left(int *arr)
{
	int tmp[42];
	int ret = 0;
	for (int i = 0; i < 42; i++)
		tmp[i] = 0;
	for (int i = 0; i < 10; i++)
	{
		arr[i] = arr[i] % 42;
		tmp[arr[i]]++;
	}
	for (int i = 0; i < 42; i++)
		if (tmp[i] != 0)
			ret++;
	return ret;
}
int main()
{
	int arr[10];
	for (int i = 0; i < 10; i++)
		scanf("%d", &arr[i]);
	printf("%d", compare_left(arr));
}