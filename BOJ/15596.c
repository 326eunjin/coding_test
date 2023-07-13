#include <stdio.h>
long long sum(int *a, int n)
{
	long long ret = 0;
	for (int i = 0; i < n; i++)
		ret += a[i];
	return ret;
}
int main()
{
	int n;
	scanf("%d", &n);
	int arr[n];
	printf("%lld", sum(arr, n));
}