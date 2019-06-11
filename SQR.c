#include<stdio.h>
int main()
{
	int a[4][2],i,j;
	for(i=0;i<4;i++)
	{
		for(j=0;j<2;j++)
		scanf("%d",&a[i][j])
	}
	if(a[0][0]!=a[1][0]||a[2][0]!=a[3][0]||a[0][1]!=a[2][1]||a[1][1]!=a[3][1])
	printf("yes");
	else
	printf("no");
	return 0;
}
