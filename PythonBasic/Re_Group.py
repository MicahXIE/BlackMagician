'''
Input Format

A single line of input containing the string S.


Output Format

Print the first occurrence of the repeating character. If there are no repeating characters, print -1.

Sample Input

..12345678910111213141516171820212223
Sample Output

1
'''

import re

# re.search not re.match, ([a-zA-Z0-9]) () must have
m = re.search(r'([a-zA-Z0-9])(\1+)', input().strip())

print(m.group(1) if m else -1)