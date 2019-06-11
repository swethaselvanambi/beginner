#include<stdio.h>
int ones(unsigned int n)
{
	int c=0;
	unsigned int m=1,a=1;
	while(m<n)
	{
		if(m&n)
			c++;
		m=m<<a;	
	}
	return c;
}
int main()
{
	int n,i,j;
	scanf("%d",&n);
	unsigned int a[n],b[n],t;
	for(i=0;i<n;i++)
		scanf("%u",&a[i]);
	for(i=0;i<n;i++)
		b[i]=ones(a[i]);
	for(i=0;i<n-1;i++)
		for(j=i+1;j<n;j++)
			if(b[i]<b[j])
			{
				t=b[i];
				b[i]=b[j];
				b[j]=t;
				t=a[i];
				a[i]=a[j];
				a[j]=t;
			}
			else if(b[i]==b[j])
			{
				if(a[i]<a[j])
				{
				t=a[i];
				a[i]=a[j];
				a[j]=t;
				}
			}
	for(i=0;i<n;i++)
	printf("%u\n",a[i]);
	return 0;
}
