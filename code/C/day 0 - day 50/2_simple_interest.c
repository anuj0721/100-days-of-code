/*
* Calculate the simple interest
* Author: Kanhaiya Ji
* Createad on September 5, 2018, 9:33PM
*/
#include<stdio.h>
int main()
{
	float p,r,t,si;
	
//	printf("Enter the value of p,r,t");
//	scanf("%f%f%f",&p,&r,&t);
	
	printf("Enter the Principle Aount p = ");
	scanf("%f",&p);
	printf("Enter the Rate of Interest r = ");
	scanf("%f",&r);
	printf("Enter the time (years) t = ");
	scanf("%f",&t);
	
	si=p*r*t/100; //formula to calculate simple interest
	
	printf("simple interest = %f Rs.",si);
	
	return 0;
	
}
