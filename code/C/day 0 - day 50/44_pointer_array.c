//use of array and pointer
#include<stdio.h>
int main()
{
	int i,a[5],*p;
	p=&a[0];
	
	printf("Enter value of 5 variables\n");
	for(i=0;i<=4;i++)
	scanf("%d",p+i);
	for(i=0;i<=4;i++)
	printf("You have entered %d\n",*(p+i));

    return 0;	
}
