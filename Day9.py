#String Split and Join

You are given a string. 
Split the string on a " " (space) delimiter and join using a - hyphen.




def split_and_join(line):
    s=line.split(" ")
    j= "-".join(s)
    return j
   
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
