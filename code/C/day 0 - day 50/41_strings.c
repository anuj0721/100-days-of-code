//strings
#include<stdio.h>
#include<string.h>
int main()
{
	char arr[]="KIETGROUPOFINSTITUTIONS";
	int len1,len2;
	
	len1=strlen(arr);
	len2=strlen("KanhaiyaJi");
	
	printf("strings = %s length = %d\n",arr,len1);
    printf("strings = %s length = %d\n","KanhaiyaJi",len2);
	
}
