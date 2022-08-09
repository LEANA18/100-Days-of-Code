#Tuples

Given an integer n and n   space-separated integers as input, create a tuple t of those n integers.
Then compute and print the result of hash(t).



n = int(input())
integer_list = map(int, input().split())
t=tuple(integer_list)
print(hash(t))

Input
*****
2
1 2

Output
******
3713081631934410656
