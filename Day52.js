#10DaysOfJavaScript
#Day3
#Arrays

Function Description
********************
Complete the getSecondLargest function in the editor below.

getSecondLargest has the following parameters:

int nums[n]: an array of integers
Returns
*******
int: the second largest number in nums

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


function getSecondLargest(nums) {
    let max=0,secondmax=0;
    let i;
    for(i=0;i<nums.length;i++)
    {
        if(nums[i]>max)
        {
            secondmax=max;
            max=nums[i];
        }
        else if(nums[i]>secondmax && nums[i]<max)
        {
            secondmax=nums[i];
        }
        
    }
    return secondmax;
}



function main() {
    const n = +(readLine());
    const nums = readLine().split(' ').map(Number);
    
    console.log(getSecondLargest(nums));
}

Input
*****
5
2 3 6 6 5

Output
******
  5
