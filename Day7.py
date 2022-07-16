#Nested Lists

Given the names and grades for each student in a class of N students, 
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
  
  
  
  if __name__ == '__main__':
    n=int(input())
    result=[]
    grade=[]
    for i in range(n):
        name = input()
        score = float(input())
        result.append([name,score])
        grade.append(score)
    grade=sorted(set(grade))
    s=grade[1]
    name=[]
    for j in result:
       if s==j[1]:
            name.append(j[0])
    name.sort()
    for ns in name:
        print(ns)    
