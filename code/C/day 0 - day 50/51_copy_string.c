//copy of string
int main()
{
	char a[50],b[50];
	
	printf("Enter string a ");
	gets(a);
	
	strcpy(b,a);
	printf("copied string is %s",b);
	return 0;
}

