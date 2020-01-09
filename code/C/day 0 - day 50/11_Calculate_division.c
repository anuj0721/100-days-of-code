/*
* calculate the division obtained by student
* created by Kanhaiya Ji	
* created on September 23, 2018, 10:54PM
*/
#include<stdio.h>
int main()
{
	int m1,m2,m3,m4,m5;
	float per;
	
	printf("Enter the marks of five subjects");
	scanf("%d%d%d%d%d",&m1,&m2,&m3,&m4,&m5);
	
	per=(m1+m2+m3+m4+m5)*100/500;
	
	if(per>=60)
		printf("First division\n");
	else if(per>=50)
		printf("Second division\n");
	else if(per>=40)
		printf("Third division\n");
	else
		printf("fail\n");
		
	return 0;
}
