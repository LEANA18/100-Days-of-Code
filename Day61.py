#Math
#TriangleQuest2
Task
****
You are given a positive integer N .
Your task is to print a palindromic triangle of size N.

For example, a palindromic triangle of size 5  is:

1
121
12321
1234321
123454321
You can't take more than two lines.

Program
*******
for i in range(1,int(input())+1): 
    print(int(((10**i-1)/9)**2))
    
Input
*****
5
Output
******
1
121
12321
1234321
123454321
