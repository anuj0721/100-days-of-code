//square of floating point nubmer usnig function
#include<stdio.h>
float square(float x);
int main()
{
	float a,b;
	printf("Enter a nubmer to find the square ");
	scanf("%f",&a);
	b=square(a);
	printf("Square is %f ",b);
	return 0;
} 
float square(float x)
{
	float y;
	y=x*x;
	return (y);
}

