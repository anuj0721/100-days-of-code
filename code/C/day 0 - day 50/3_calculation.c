/*
* File: program to calculate add,sub,mul,division
* Author: Kanhaiya Ji
* Created on September 6, 2018, 10:17PM
*/
#include<stdio.h>
int main()
{
	float x,y,add,sub,mul,div;
	
	printf("Calculate addition,substraction,multiplication,division of two numbers...\n\n");
	
	printf("Enter the value of x = ");
	scanf("%f",&x);
	
	printf("Enter the value of y = ");
	scanf("%f",&y);
	
	add=x+y;
	sub=x-y;
	mul=x*y;
	div=x/y;
	
	printf("addition = %f\n",add);
	printf("subtraction = %f\n",sub);
	printf("multiply = %f\n",mul);
	printf("division = %f\n",div);
	
	return(0);
	
}

