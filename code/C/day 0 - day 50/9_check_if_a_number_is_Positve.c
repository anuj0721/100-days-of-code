/*
* Program to check whether a number is positive or not
* Created by Kanhaiya Ji
* Created on September 12, 2018, 9:59PM
*/
#include<stdio.h>
int main()
{
	int x;
	
	printf("Enter a number:");
	scanf("%d",&x);
	
	if(x>0)
	{
		printf("Number is positive");
	}
	if(x<=0)
	{
		printf("Number is Non Positive");
	}
}
