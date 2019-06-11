#include<stdio.h>
int main()
{
	long int n;
	scanf("%ld",&n);
	if(n==0)
	printf("Zero");
	else if(n>0)
	printf("Positive");
	else
	printf("Negative");
	return 0;
}
