/* whether driver should insured or not
* created by Kanhaiya Ji	
* created on September 23, 2018, 10:54PM
*/
#include<stdio.h>
int main()
{
	char ms,sex;
	int age;
	
	printf("Enter Marital Status,Sex,Age");
	scanf("%c%c%d",&ms,&sex,&age);
	
	if((ms=='M')||(ms=='U' && sex=='M' && age>30)||(ms=='U' && sex=='F' && age>25))
		printf("Driver should be insured\n");
	else
		printf("Driver should not be insured");
		
	return 0;
}
