#Math 
#Triangle Quest
You are given a positive integer n. Print a numerical triangle of height n-1 like the one below:
1
22
333
4444
55555
Can you do it using only arithmetic operations, a single for loop and print statement?


for i in range(1,int(input())): 
    print((pow(10,i)//9)*i)
