//Entry to a place if name is on the list
#include<stdio.h>
#include<string.h>
#define FOUND 1
#define NOTFOUND 0
int main()
{
	char masterlist[6][9]=
							{
								"Kanhaiya"
								"Akshay"
								"Bhanu"
								"Pravin"
								"Deepak"
								"Vipul"
							};
			
	int i,flag,a;
	char yourname[15];
	
	printf("Enter your name ");
	scanf("%s",yourname);	
	
	flag=NOTFOUND;
	for(i=0;i<=5;i++)
	{
		a=strcmp(&masterlist[i][0],yourname);	
		if(a==0)
		{
			printf("welcome,you can enter the palace\n");
			flag=FOUND;
			break;
		}
		if(flag==NOTFOUND)
		printf("Sorry,you can not enter the palace\n");
		return 0;
	}	
	
}
