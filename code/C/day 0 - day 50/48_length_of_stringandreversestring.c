//find length of string
#include<stdio.h>
#include<string.h>
void reverse(char*, int, int);
int main()
{
	char s[50];
	int length;
	
	printf("Enter a string to find its length ");
	gets(s);
	
	length=strlen(s);
	printf("Length of string=%d\n",length);
	
	reverse(s,0,length-1);
	printf("reverse of string is %s",s);
	
	return 0;
}
void reverse(char *x, int begin, int end)
{
   char c;
 
   while(begin<end){
   		c=*(x+begin);
   		*(x+begin)=*(x+end);
   		*(x+end)=c;
   		begin++;
   		end--;
   }
}
