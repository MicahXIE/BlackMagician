'''
A valid mobile number is a ten digit number starting with a 7,8 or 9.

Input Format

The first line contains an integer N, the number of inputs.
N lines follow, each containing some string.


Output Format

For every string listed, print "YES" if it is a valid mobile number and "NO" if it is not on separate lines. Do not print the quotes.

Sample Input

2
9587456281
1252478965
Sample Output

YES
NO
'''

import re

regex_pattern = '^[7|8|9][0-9]{9}$'

n = int(input().strip())

for _ in range(n):
    print('YES' if re.match(regex_pattern, input()) else 'NO')

