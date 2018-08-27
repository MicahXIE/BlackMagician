'''
Sample Input

11
#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
}   
Sample Output

#FfFdF8
#aef
#f9f9f9
#fff
#ABC
#fff
Explanation

#BED and #Cab satisfy the Hex Color Code criteria, but they are used as selectors and not as color codes in the given CSS.

Hence, the valid color codes are:

#FfFdF8
#aef
#f9f9f9
#fff
#ABC
#fff
'''

import re

regex_pattern = '#[0-9a-fA-F]{3,6}'

n = int(input().strip())

s = ""
flag = 0
for _ in range(n):
    s1 = input().strip()
    if flag == 1:
        s += (s1 + '\n')
    if '{' in s1:
        flag = 1
    if '}' in s1:
        flag = 0
    
#re.match re.search re.search re.findall re.finditers re.S re.DOTALL    
matches = re.findall(regex_pattern, s, re.S)
print(*matches, sep='\n')
