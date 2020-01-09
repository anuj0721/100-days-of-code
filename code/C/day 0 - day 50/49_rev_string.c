#include<stdio.h>
int main()
{
	char s[50],rev;
	printf("Enter string to reverse it ");
	gets(s);
	
	rev=strrev(s);
	printf("reverse of string is ");
	puts(s);
}
