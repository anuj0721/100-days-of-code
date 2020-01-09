#include<stdio.h>
int main()
{
	char a[50],b[50],cmp;
	printf("Enter string a ");
	gets(a);
	printf("Enter string b ");
    gets(b);
	
	cmp=strcmp(a,b);
	printf("comparison is %s",cmp);
	return 0;	
}
