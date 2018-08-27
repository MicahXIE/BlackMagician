'''
A valid email address meets the following criteria:

It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the following: alphanumeric characters, -,., and _.
The domain and extension contain only English alphabetical characters.
The extension is 1, 2, or 3 characters in length.

import email.utils
print email.utils.parseaddr('DOSHI <DOSHI@hackerrank.com>')
print email.utils.formataddr(('DOSHI', 'DOSHI@hackerrank.com'))
produces this output:

('DOSHI', 'DOSHI@hackerrank.com')
DOSHI <DOSHI@hackerrank.com>

Sample Input

2  
DEXTER <dexter@hotmail.com>
VIRUS <virus!@variable.:p>
Sample Output

DEXTER <dexter@hotmail.com>
'''

import email.utils
import re

#username@domain.extension
username = '[a-zA-Z]([a-zA-Z0-9_|\-|\.]+)'
domain = '([a-zA-Z]+)'
extension = '[a-zA-Z]{1,3}'

regex_pattern = '^'+username+'@'+domain+'\.'+extension+'$'

n = int(input())

for _ in range(n):
    tp = email.utils.parseaddr(input().strip())
    s = email.utils.formataddr(tp)
    s_lst = s.strip().split()
    #print(regex_pattern)
    #print(*s_lst)
    #print(re.match(regex_pattern, s_lst[1][1:-1]))
    if re.match(regex_pattern, s_lst[1][1:-1]):
        print(s)