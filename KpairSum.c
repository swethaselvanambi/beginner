#include<stdio.h>
int main()
{
	int n,k,i,j,f=0;
	scanf("%d%d",&n,&k);
	int a[n];
	for(i=0;i<n;i++)
		scanf("%u",&a[i]);
	for(i=0;i<n-1&&f==0;i++)
		for(j=i+1;j<n;j++)
			if(a[i]+a[j]==k)
			{
				f=1;
				printf("yes");
				break;
			}
	if(f==0)
	printf("no");
	

	return 0;
}
