/*
* Calculation of toral expenses
* Created By Kanhaiya Ji
* Created on September 16, 2018,9:17PM
*/
#include<stdio.h>
int main()
{
	int qty,dis=0;
	float price,texp;
	printf("Enter the quantiy of item ");
	scanf("%d",&qty);
	printf("Enter the price of 1 item ");
	scanf("%f",&price);
	
	if(qty>1000)
	{
		dis=10;
	}
	
	
	texp=(qty*price)-(qty*price*dis/100);
	printf("Total Expense = RS.%f",texp);
	
	return 0;
	
}
