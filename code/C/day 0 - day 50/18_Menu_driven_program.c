/*Menu driven program*/
#include<stdio.h>
#include<stdlib.h>
int main()
{
	char choice;
	int a,b,c,n,d;
	while(1)
	{
	printf("1.Addition\n");
	printf("2.Odd_Even\n");
	printf("3.Print_n_numbers\n");
	printf("4.Exit");
	
	printf("\nPlease Enter your choice ");
	scanf("%d",&choice);

	switch(choice)
	{
		case 1:
			printf("Enter two numbers ");
			scanf("%d%d",&a,&b);
			printf("Addition is %d\n\n",a+b);
			break;
		case 2:
			printf("Enter a number ");
			scanf("%d",&n);
			if(n%2==0)
			{
				printf("%d is even\n\n",n);
				break;
			}
			else
			{
				printf("%d is odd\n\n",n);
				break;
			}
				
		case 3:
			printf("Enter a Number to which you want to print numbers ");
			scanf("%d",&c);
			for(d=1;d<=c;d++)
			{
				printf("%d\n",d);
			}
			break;
		case 4:
			exit(0);
		default:
			printf("you have entered a wrong choice! please enter a valid choice\n\n");
			
	}		
    }
}
