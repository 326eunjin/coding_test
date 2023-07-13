#include <stdio.h>
int min(int arr[],int count)
{
	int tmp=arr[0];
	for(int i=0;i<count;i++)
		if(tmp>=arr[i])
			tmp=arr[i];
	return tmp;
}
int max(int arr[],int count)
{
	int tmp=arr[0];
	for(int i=0;i<count;i++)
		if(tmp<=arr[i])
			tmp=arr[i];
	return tmp;
}
int main()
{
	int num;
	scanf("%d",&num);
	int a[num];
	for(int i=0;i<num;i++)
		scanf("%d",&a[i]);
	printf("%d %d",min(a,num),max(a,num));
}