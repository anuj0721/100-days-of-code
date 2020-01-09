#include<stdio.h>
int rstrptr(int a,int b);
int main()
{
	int i,j;
	for(i=1;i<=5;i++)
	{
		for(j=1;j<=5;j++)
		{
			if(j<=i)
				printf("*");
			else
				printf(" ");
		}
		printf("\n");
	}
	printf("\n");
	rstrptr(i,j);
	return 0;
}   
int rstrptr(int a,int b)
{
	int i,j;
		for(i=1;i<=5;i++)
	{
		for(j=1;j<=5;j++)
		{
			if(j<=6-i)
				printf("*");
			else
				printf(" ");
		}
		printf("\n");
	}
	printf("\n");
	
}
