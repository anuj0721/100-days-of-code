/*
* File : Program to check Even or odd
* Author: Kanhaiya Ji
* Created on September 9, 2018, 4:28PM
*/
#include<stdio.h>
int main()
{
  int x;
  
  printf("Enter a Number to Check Even or Odd- ");
  scanf("%d",&x);
  
  if(x%2==0)
  {
  	printf("%d is Even",x);
  }
  else
  {
  	printf("%d is odd",x);
  }
}
