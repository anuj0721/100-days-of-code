//use of macro 
#include<stdio.h>
#define AND &&
#define cond1 (f<5)
#define cond2 (x<=20 || y<=45)
int main()
{
	int f,x,y;
	
	printf("Enter the value of F between 1 and 5 ");
	scanf("%d",f);
	printf("Enter the value of x between 1 and 20 ");
	scanf("%d",x);
	printf("Enter the value of y between 1 and 90 ");
	scanf("%d",y);
	if((cond1) AND (cond2))
	{
		printf("What an obedient servent you are\n");
	}
	else
	{
		printf("You have entered the wrong value!\nPlease Enter valid values..");
	}
	return 0;
}
