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
  
/* Here I performed bitwise and operaiton between x and 1.
 * If a Binary Number is Even then its last digit will be 0, and if odd last digit will be 1,so here i make use of this property
 * suppose if a number is odd then it's last digit will be 1 so operation will be 1 & 1. that will return 1(true)
*/ 
  if(x&1) 
  {
  	printf("%d is odd",x);
  }
  else
  {
  	printf("%d is even",x);
  }
}
