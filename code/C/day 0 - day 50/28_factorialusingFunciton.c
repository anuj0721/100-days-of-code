//factorial using function
#include<stdio.h>
int factorial(int x);
int main()
{
	int a,fact;
	printf("Enter any number ");
	scanf("%d",&a);
	fact=factorial(a);
	printf("factorail is %d\n",fact);
	return 0;
}
int factorial(int x)
{
	int f=1,i;
	for(i=x;i>=1;i--)
	f=f*i;
	return(f);
}
