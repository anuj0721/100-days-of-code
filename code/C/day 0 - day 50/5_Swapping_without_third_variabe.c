/* 
* File: Swapping of two variables without using third varaible
* Author: Kanhaiya Ji
* Created on August 07,	2018, 10:17PM
*/
#include<stdio.h>
int main()
{
	int a,b;
	
	printf("Enter first Number a = ");
	scanf("%d",&a);
	
	printf("Enter Second Number b = ");
	scanf("%d",&b);
	
	a=a+b;
	b=a-b; 
	a=a-b;
	
	printf("After Swapping\n");
	
	printf("Value of a = %d\n",a);
    printf("Value of b = %d",b);
	
	return 0;	
}
