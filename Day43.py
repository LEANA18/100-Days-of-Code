#30DaysofCode
#Let's Review

Task
****
Given a string S of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters as 2  space-separated strings on a single line 

Program
*******
n=int(input())
temp=[]
for i in range(0,n):
    s=input()
    temp.append(s)
for i in range(0,n):
    for j in range(0,len(temp[i]),2):
        print(temp[i][j],end='')
    print(end=' ')
    for j in range(1,len(temp[i]),2):
        print(temp[i][j],end='')
    print()
    
Input
*****
2
Hacker
Rank

Output
******
Hce akr
Rn ak

