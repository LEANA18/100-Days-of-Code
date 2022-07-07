Given an integer,n , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5 ,print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than , print Not Weird


import math
import os
import random
import re
import sys
n=int(input())
if n%2!=0:
    print("Weird")
else:
    if n in range(2,6):
        print("Not Weird")
    elif n in range(6,21):
        print("Weird")
    elif n>20:
        print("Not Weird")
