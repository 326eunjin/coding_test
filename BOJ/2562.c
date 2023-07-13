#include <stdio.h>
int max(int arr[])
{
	int tmp = arr[0];
	for (int i = 0; i < 9; i++)
		if (tmp <= arr[i])
			tmp = arr[i];
	return tmp;
}
int max_location(int arr[], int max)
{
	for (int i = 0; i < 9; i++)
		if (max == arr[i])
			return (i + 1);
	return 0;
}
int main()
{
	int arr[9];
	for (int i = 0; i < 9; i++)
		scanf("%d\n", &arr[i]);
	printf("%d\n", max(arr));
	printf("%d", max_location(arr, max(arr)));
}