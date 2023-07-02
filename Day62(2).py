#Algorithms
#SimpleArraySum

Task
****
Given an array of integers, find the sum of its elements.
Complete the simpleArraySum function in the editor below. It must return the sum of the array elements as an integer.

simpleArraySum has the following parameter(s):

ar: an array of integers

Program
*******
import math
import os
import random
import re
import sys

def simpleArraySum(ar):
    sum=0
    for element in ar:
        sum+=element
    return sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

Input
*****
6
1 2 3 4 10 11

Output
******
31
