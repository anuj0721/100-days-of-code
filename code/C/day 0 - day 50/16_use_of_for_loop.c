/*simple interest 3 times using for loop*/
#include<stdio.h>
int main()
{
	int p,t,count;
	float r,si;
	
	for(count=1;count<=3;count=count+1)
	{
		printf("Enter values of p,r,t");
		scanf("%d%f%d",&p,&r,&t);
		si=p*r*t/100;
		printf("simple interest = Rs.%f\n\n",si);
	}
	return 0; 
}
