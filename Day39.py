#30DaysOfCode
#Operators

Task
****
Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip),
and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost. 
Round the result to the nearest integer.

int meal_cost: the cost of food before tip and tax
int tip_percent: the tip percentage
int tax_percent: the tax percentage

meal_cost=12
tip_percent=20
tax_percent=8

tip=12*20/100=2.4
tax=12*8/100=0.96
total_cost=meal_cost+tip+tax
          =12+2.4+0.96
          = 15.26
    
 round(total_cost)=15
We round total_cost to the nearest integer and we print the result.

Program
********
import math
import os
import random
import re
import sys

def solve(meal_cost, tip_percent, tax_percent):
    tip=meal_cost*tip_percent/100
    tax=meal_cost*tax_percent/100
    total_cost=meal_cost+tip+tax
    print(round(total_cost))
if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())
    solve(meal_cost, tip_percent, tax_percent)
    
    
    
Input
*****
12.00
20
8

Output
******
15

