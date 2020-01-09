#include<stdio.h>
void bhanu();
void kanhaiya();
void delhi();
int main()
{
	printf("This is KIET\n");
	bhanu();
	kanhaiya();
	delhi();
	printf("I am back in main funciton\n");
	
	return 0;
}
void bhanu()
{
	printf("Hello i am  Bhanu\n");
}
void kanhaiya()
{
	printf("Hello i am  Kanhaiya\n");
	bhanu();
}
void delhi()
{
	printf("this is National capital region\n");
}
