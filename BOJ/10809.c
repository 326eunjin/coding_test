#include <stdio.h>
void loc_alpha(int *arr, char *str)
{
	int count=0;
	while(str[count])
	{
		int tmp=str[count]-97;
		if(arr[tmp]==-1)
			arr[tmp]=count;
		count++;
	}
	for(int i=0;i<26;i++)
		printf("%d ",arr[i]);
}
int main()
{
	int alpha[26];
	for(int i=0;i<26;i++)
		alpha[i]=-1;
	char str[100];
	scanf("%s",str);
	loc_alpha(alpha,str);
}