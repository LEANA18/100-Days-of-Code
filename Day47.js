#10DaysOfJavaScript
#Day1
#Functions

Task
****
Implement a function named factorial that has one parameter: an integer,n. It must return the value of n! (i.e.,n factorial).

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
function factorial(n)
{
    let fact=1;
    for(let i=1;i<=n;i++)
    {
        fact=fact*i;
    }
    return fact;
}



function main() {
    const n = +(readLine());
    
    console.log(factorial(n));
}

Input
*****
  4
Output
******
  24
