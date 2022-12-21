#Math
#Polar Coordinates

Polar coordinates are an alternative way of representing Cartesian coordinates or Complex Numbers.
A complex number z   z=x+yj
is completely determined by its real part x and imaginary part y.
Here, j is the imaginary unit.
If we convert complex number  to its polar coordinate, we find:
r: Distance from z to origin, i.e., 
theta: Counter clockwise angle measured from the positive -axis to the line segment that joins  to the origin.

Python's cmath module provides access to the mathematical functions for complex numbers.
cmath.phase
***********
This tool returns the phase of complex number z  (also known as the argument of ).

>>> phase(complex(-1.0, 0.0))
3.1415926535897931

abs
***
This tool returns the modulus (absolute value) of complex number z .

>>> abs(complex(-1.0, 0.0))
1.0

Task
****
You are given a complex z . Your task is to convert it to polar coordinates.

Input Format
*************

A single line containing the complex number z . Note: complex() function can be used in python to convert the input as a complex number.
  
Program
*******
import cmath

z=complex(input().strip())
result=cmath.polar(z)
print(result[0])
print(result[1])


OR

import cmath

z=input()
a=abs(complex(z))
r=cmath.phase(complex(z))
print(a)
print(r)

Input
******
1+2j

Output
******

 2.23606797749979 
 1.1071487177940904



