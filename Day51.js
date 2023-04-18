#10DaysOfJavaScript
#Day2
#Loops

Task
****
First, print each vowel in s on a new line. The English vowels are a, e, i, o, and u, and each vowel must be printed in the same order as it appeared in s .
Second, print each consonant (i.e., non-vowel)  in s on a new line in the same order as it appeared in s .

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
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    let i;
    let c;
    let v;
    for(i=0;i<=s.length-1;i++)
    {
        v=s.charAt(i);
        if(v=='a'||v=='e'||v=='i'||v=='o'||v=='u'||v=='A'||v=='E'||v=='I'||v=='O'||v=='U')
        {
           console.log(v); 
        }
    }
    for(i=0;i<=s.length-1;i++)
    {
        c=s.charAt(i);
         if(c=='b'||c=='c'||c=='d'||c=='f'||c=='g'||c=='h'||c=='j'||c=='k'||c=='l'||c=='m'||c=='n'||c=='p'||c=='q'||c=='r'||c=='s'||c=='t'||c=='v'||c=='w'||c=='x'||c=='y'||c=='z'||c=='B'||c=='C'||c=='D'||c=='F'||c=='G'||c=='H'||c=='J'||c=='K'||c=='L'||c=='M'||c=='N'||c=='P'||c=='Q'||c=='R'||c=='S'||c=='T'||c=='V'||c=='W'||c=='X'||c=='Y'||c=='Z')
        {
            console.log(c);
        }
    }
       
    }



function main() {
    const s = readLine();
    
    vowelsAndConsonants(s);
}

Input
*****
  javascriptloops

Output
******
a
a
i
o
o
j
v
s
c
r
p
t
l
p
s
