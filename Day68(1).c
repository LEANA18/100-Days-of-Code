Task
****
Your task is to take two numbers of int data type, two numbers of float data type as input and output their sum:

Declare 4 variables: two of type int and two of type float.
Read 2  lines of input from stdin (according to the sequence given in the 'Input Format' section below) and initialize your 4 variables.
Use the + and -  operator to perform the following operations:
Print the sum and difference of two int variable on a new line.
Print the sum and difference of two float variable rounded to one decimal place on a new line.

Program
*******
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int num1,num2;
    float num3,num4,sum,diff;
	scanf("%d%d",&num1,&num2);
    scanf("%f%f",&num3,&num4);
    printf("%d %d\n",num1+num2,num1-num2);
    sum=num3+num4;
    diff=num3-num4;
    printf("%.1f %.1f",sum,diff);
    
    return 0;
}

Input
*****
10 4
4.0 2.0
Output
******
14 6
6.0 2.0
