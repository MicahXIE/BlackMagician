'''
ABC = 90°

Point M is the midpoint of hypotenuse AC.
You are given the lengths AB and BC. 
Your task is to find  MBC in degrees.

Input Format

The first line contains the length of side AB.
The second line contains the length of side BC.

Output Format

Output MBC in degrees.

Sample Input
10
10

Sample Output
45°
'''

'''
example:
>>> round(2.5)
2
>>> round(3.5)
4
>>> round(4.5)
4

mac:
shift + option + 8 -> '°'
'''

import math

if __name__ == "__main__":
    
    AB = int(input())
    BC = int(input())
    
    AC = math.sqrt(AB**2 + BC**2)
    BM = AC / 2.0
    h = BC / 2.0 
    
    print(str(int(round(math.degrees(math.acos(h/BM))))) + '°')