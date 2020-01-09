/*
* File: swapping of two integers/float
* Author: Kanhaiya Ji
* Created on September 6, 2018, 10:47PM
*/
#include<stdio.h>
int main()
{
	float a,b,c;
	
	printf("Enter the value of a = ");
	scanf("%f",&a);
	
	printf("Enter the value of b = ");
	scanf("%f",&b);
	
	c=a;
	a=b;
	b=c;
	
	printf("After swapping value of a = %f\n",a);
	printf("After swapping value of b = %f",b);
	
	return(0);
	
}
