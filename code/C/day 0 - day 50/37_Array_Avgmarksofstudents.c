//average marks of 30 students
#include<stdio.h>
int main()
{
	int i,avg,sum=0;
	int marks[30]; //arrey declaration
	
	for(i=0;i<=29;i++)
	{
		printf("Enter marks ");
		scanf("%d",&marks[i]);
	}
	for(i=0;i<=29;i++)
	{
		sum=sum+marks[i];
	}
	avg=sum/30;
	printf("Average Marks=%d\n",avg);
	return 0;
}
