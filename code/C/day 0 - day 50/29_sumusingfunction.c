#include<stdio.h>
int add(int x,int y);
int main()
{
    int a,b,c;
	printf("Enter two numbers\n");
	scanf("%d%d",&a,&b);
	c=add(a,b);
	printf("sum = %d",c);
	return 0;
}
int add(int x,int y)
{
	int sum;
	sum=x+y;
	return (sum);
}
