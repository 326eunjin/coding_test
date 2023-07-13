#include <stdio.h>
void score(int *arr, int input, char *str)
{
	for (int j = 0; j < input; j++)
	{
		int i = 0;
		int ret = 0;
		int tmp = 1;
		scanf("%s", str);
		while (str[i])
		{
			if (str[i] == 'O')
			{
				ret = ret + tmp;
			}
			if (str[i] == 'O' && str[i + 1] == 'O')
				tmp++;
			else
				tmp = 1;
			i++;
		}
		arr[j] = ret;
	}
	for (int j = 0; j < input; j++)
		printf("%d\n", arr[j]);
}
int main()
{
	char str[80];
	int input;
	scanf("%d", &input);
	int arr[input];
	score(arr, input, str);
}