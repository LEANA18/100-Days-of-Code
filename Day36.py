#Strings
#The Minion Game

Kevin and Stuart want to play the 'The Minion Game'.

Game Rules
**********
Both players are given the same string s .
Both players have to make substrings using the letters of the string s .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string s.

For Example:
String s = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

Your task is to determine the winner of the game and their score.

Function Description
*******************

Complete the minion_game in the editor below.

minion_game has the following parameters:

string string: the string to analyze
Prints
******
string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
Input Format
***********
A single line of input containing the string s .
Note: The string  will contain only uppercase letters: A-Z

Program
*******
def minion_game(s):
    s1=0
    s2=0
    vow='AEIOU'
    for i in range(len(s)):
        if s[i] not in vow:
            s1=s1+(len(s)-i)
        else:
            s2=s2+(len(s)-i)
    if s1>s2:
        print("Stuart",s1)
    elif s2>s1:
        print("Kevin",s2)
    else:
        print("Draw")
    

if __name__ == '__main__':
    s = input()
    minion_game(s)
    
Input
*****
BANANA

Output
******
Stuart 12
