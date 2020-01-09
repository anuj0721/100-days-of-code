/*use of switch case*/
#include<stdio.h>
int main()
{
	char ch;
	printf("Enter any one of the alphabets a,b,or c");
	scanf("%c",&ch);
	switch(ch)
	{
		case 'a':
		case 'A':
			printf("a as in apple");
			break;
		case 'b':
		case 'B':
			printf("b as brain");
			break;
		case 'c':
		case 'C':
			printf("c as cookie");
			break;
		defualt:
			printf("wish u know what are alphabets\n");
	return 0;
	}
}
