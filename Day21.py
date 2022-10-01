#Sets
#Introduction to sets

Ms. Gabriel Williams is a botany professor at District College. 
One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

Formula used:
  Average = Sum of distinct heights/Total number of distinct heights
  
  
  
  
   average(array):
    s=sum(set(array))
    l=len(set(array))
    average=s/l
    return average
   
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
  
  
  Input
  *****
  STDIN                                       Function
-----                                       --------
10                                          arr[] size N = 10
161 182 161 154 176 170 167 171 170 174     arr = [161, 181, ..., 174]

Output
******
169.375


 Using the sum() and len() functions, we can compute the average.
  Average=1355/8=169.375



