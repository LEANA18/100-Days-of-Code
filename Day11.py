#Basic Datatypes


The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
  Print the average of the marks array for the student name provided, showing 2 places after the decimal.
  
  Sample input
  ***********
 3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Sample Output
*************
56.00
  
  
  if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks=student_marks[query_name]
    avg=format(sum(marks)/3,'.2f')
    print(avg)
    
