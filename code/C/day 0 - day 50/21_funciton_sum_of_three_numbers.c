// sum of three numbers using funciotn
#include<stdio.h>
int calsum(int x,int y,int z);
int main()
{
	int a,b,c,d,sum;
	printf("Enter any three numbers\n");
	scanf("%d%d%d",&a,&b,&c);
	sum=calsum(a,b,c);
	printf("Sum= %d\n",sum);
	return 0;
}
int calsum(int x,int y,int z)
{
	int d;
	d=x+y+z;
	return (d);
	
}
