Chef wants to appear in a competitive exam. To take the exam, there are following requirements:

Minimum age limit is X (i.e. Age should be greater than or equal to X).
Age should be strictly less than Y.
Chef's current Age is A. Find whether he is currently eligible to take the exam or not.

Input Format
************

First line will contain TT, number of test cases. Then the test cases follow.
Each test case consists of a single line of input, containing three integers X, Y and A as mentioned in the statement.

Output Format
*************
For each test case, output YES if Chef is eligible to give the exam, NO otherwise.

T=int(input())
for i in range(T):
    X,Y,A=map(int,input().split())
    if(A>=X and A<Y):
        print("YES")
    else:
        print("NO")
            
          
Input
*****
5
21 34 30
25 31 31
22 29 25
20 40 15
28 29 28

Output
******
YES
NO
YES
NO
YES

