'''
Input Format

A single line containing the complex number z. Note: complex() function can be used in python to convert the input as a complex number.

Constraints

Given number is a valid complex number

Output Format

Output two lines: 
The first line should contain the value of r. 
The second line should contain the value of t.

Sample Input:
1+2j

Sample Output:
2.23606797749979 
1.1071487177940904

follow-up:
re summary
print summary
* usage

'''

import cmath
import re

#input method
x = complex(input())

#reg_exp = r"(-?\d+)\+?(\-?\d+)j"
#majObj = re.match(reg_exp,input())
#a = int(majObj.group(1))
#b = int(majObj.group(2))
#x = complex(a, b)


#print method
#print(abs((x)))
#print(cmath.phase((x)))

#r, t = cmath.polar(x)
#print ("{0}\n{1}".format(r,t))

#print(*cmath.polar(x), sep='\n')
print("{}\n{}".format(*cmath.polar(x)))