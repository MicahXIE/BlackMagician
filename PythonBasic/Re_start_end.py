'''
Sample Input

aaadaa
aa
Sample Output

(0, 1)  
(1, 2)
(4, 5)

'''
# solution 1
import re

org_str = input().strip()
sub_str = input().strip()

org_len = len(org_str)
sub_len = len(sub_str)

lst = []
for i in range(org_len - sub_len + 1):
    if org_str[i:i+sub_len] == sub_str:
        tp = (i,i+sub_len-1)
        lst.append(tp)

if not lst:
    print((-1,-1))
else:
    print(*lst, sep='\n')


# solution 2
# search method
import re

s = input()
k = input()
pattern = re.compile(k)
r = pattern.search(s)
if not r: print("(-1, -1)")
while r:
    print("({0}, {1})".format(r.start(), r.end() - 1))
    r = pattern.search(s,r.start() + 1)