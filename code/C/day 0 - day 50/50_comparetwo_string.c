//comparison between two strings
#include<stdio.h>
int main()
{
	char a[50],b[50];
	int cmp;
	printf("Enter string a ");
	gets(a);
	printf("Enter string b ");
    gets(b);
	
	cmp=strcmp(a,b);
    if(cmp=0)
    {
    	printf("string matched");
	}
	else
	{
		printf("string not matched");
	}
	//printf("comparison is %d",cmp);
	return 0;	
}
