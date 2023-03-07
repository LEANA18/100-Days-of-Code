#JavaScript
#10DaysOfJavaScript
#Day 0
#Hello,World!


Task
****
A greeting function is provided for you in the editor below. It has one parameter,parameterVariable . Perform the following tasks to complete this challenge:

Use console.log() to print Hello, World! on a new line in the console, which is also known as stdout or standard output. The code for this portion of the task is already provided in the editor.
Use console.log() to print the contents of parameterVariable (i.e., the argument passed to main).


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

/**
*   A line of code that prints "Hello, World!" on a new line is provided in the editor. 
*   Write a second line of code that prints the contents of 'parameterVariable' on a new line.
*
*	Parameter:
*   parameterVariable - A string of text.
**/
function greeting(parameterVariable) {
    // This line prints 'Hello, World!' to the console:
    console.log('Hello, World!');
    console.log(parameterVariable)
    // Write a line of code that prints parameterVariable to stdout using console.log:
    
}


function main() {
    const parameterVariable = readLine();
    
    greeting(parameterVariable);
}

Input
*****
  Welcome to 10 Days of JavaScript!
    
 Output
*******
  Hello, World!
Welcome to 10 Days of JavaScript!
