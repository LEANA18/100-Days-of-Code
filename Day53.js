#10DaysOfJavaScript
#Day3
#Try, Catch and Finally

Task
****
Complete the reverseString function; it has one parameter,s. You must perform the following actions:

Try to reverse string s using the split, reverse, and join methods.
If an exception is thrown, catch it and print the contents of the exception's message on a new line.
Print s on a new line. If no exception was thrown, then this should be the reversed string; if an exception was thrown, this should be the original string.

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


function reverseString(s) {
    try
    {
        var splitstring=s.split("");
        var reversestring=splitstring.reverse();
        var joinstring=reversestring.join("");
        console.log(joinstring);
        return joinstring;
        
    }
    catch
    {
        console.log("s.split is not a function");
        console.log(s);
        return s;
    }
}


function main() {
    const s = eval(readLine());
    
    reverseString(s);
}

Input 1
********
  "1234"

Output 1
********
  4321

Input 2
*******
  Number(1234)

Output 2
********
  s.split is not a function
1234
