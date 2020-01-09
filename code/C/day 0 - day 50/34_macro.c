//Area of circle
#include<stdio.h>
#define PI 3.14
#define show printf("Area of circle=%f",area);
int areaof(float x);
int main()
{
	float r,area;
	printf("Enter radius of Circle ");
	scanf("%f",&r);
    area=areaof(r);
	show
	return (0);
}
int areaof(float x)
{
	float totle;
	totle=PI*x*x;
	return(totle);
}
