/*simple interest for 3 steps*/
#include<stdio.h>
int main()
{
	int p,t,count;
	float r,si;
	
	count=1;
	while(count<=3)
	{
		printf("Enter values of p,r,t");
		scanf("%d%f%d",&p,&r,&t);
		si=p*r*t/100;
		printf("simple interest = Rs.%f\n\n",si);
		
		count=count+1;
	}
	return 0;
}
