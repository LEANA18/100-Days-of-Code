Chef considers the climate HOT if the temperature is above 20, otherwise he considers it COLD. 
You are given the temperature C, find whether the climate is HOT or COLD.

x=int(input())
for i in range(1,x+1):
    C=int(input())
    if C<=20:
        print("COLD")
    else:
        print("HOT")


