'''
You are given a string S. Suppose a character 'c' occurs consecutively X times in the string. 
Replace these consecutive occurrences of the character 'c' with (X, c) in the string.

For a better understanding of the problem, check the explanation.

Input Format

A single line of input consisting of the string S.

Output Format

A single line of output consisting of the modified string.


Sample Input:
1222311

Sample Output:
(1, 1) (3, 2) (1, 3) (2, 1)

Explanation

First, the character 1 occurs only once. It is replaced by (1, 1). Then the character 2 occurs three times, 
and it is replaced by (3,2) and so on.
Also, note the single space within each compression and between the compressions.

'''

from itertools import groupby

s = input().strip()

for key, group in groupby(s):
    item = '('+str(len(list(group)))+', '+key+')'
    print(item, end=' ')