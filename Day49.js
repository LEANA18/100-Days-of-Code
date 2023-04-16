#10DaysOfCode
#Day2
#Conditional Statements:if-else

Task
****
Complete the getGrade(score) function in the editor. It has one parameter: an integer score denoting the number of points Julia earned on an exam.
It must return the letter corresponding to her grade according to the following rules:

If 25>score>=30 then grade=A.
If 20>score>=25, then grade=B.
If 15>score>=20, then grade=C.
If 10>score>=15, then grade=D.
If 5>score>=10, then grade=E.
If 0>=score>=5, then grade=F.

Program
*******
  'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

function getGrade(score) {
    let grade;
   if(score > 25)
   {
       grade="A";
   }
   else if(score > 20)
   {
       grade="B";
   }
   else if(score > 15)
   {
       grade="C";
   }
   else if(score > 10)
   {
       grade="D";
   }
   else if(score > 5)
   {
       grade="E";
   }
   else 
   {
       grade="F";
   }
    return grade;
}


function main() {
    const score = +(readLine());
    
    console.log(getGrade(score));
}

Input
*****
  11
Output
******
  D
