#include <stdio.h>
int max(int *arr, int num)
{
	int tmp = arr[0];
	for (int i = 0; i < num; i++)
		if (tmp <= arr[i])
			tmp = arr[i];
	return tmp;
}
float new_score(int *arr, int max, int num)
{
	float avg = 0;
	for (int i = 0; i < num; i++)
		avg += arr[i];
	avg = avg / num;
	avg = avg / max * 100;
	return avg;
}
int main()
{
	int count;
	scanf("%d", &count);
	int subject[count];
	for (int i = 0; i < count; i++)
		scanf("%d", &subject[i]);
	printf("%.6f", new_score(subject, max(subject, count), count));
}