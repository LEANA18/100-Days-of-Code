#10DaysOfJavascript
#Day4
#Count Objects

Task
*****
Complete the function in the editor.
It has one parameter: an array a  of objects. 
Each object in the array has two integer properties denoted by x and y. 
The function must return a count of all such objects o in array a that satisfy o.x==o.y.

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

/*
 * Return a count of the total number of objects 'o' satisfying o.x == o.y.
 * 
 * Parameter(s):
 * objects: an array of objects with integer properties 'x' and 'y'
 */
function getCount(objects) {
    let i,count=0;
    for(const i in objects)
    {
        if(objects[i].x==objects[i].y)
        {
            count+=1;
        }
    }
    return count;
    
    
}


function main() {
    const n = +(readLine());
    let objects = [];
    
    for (let i = 0; i < n; i++) {
        const [a, b] = readLine().split(' ');
        
        objects.push({x: +(a), y: +(b)});
    }
    
    console.log(getCount(objects));
}

Input
*****
  5
1 1
2 3
3 3
3 4
4 5

Output
******
  2

