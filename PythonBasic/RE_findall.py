'''
Sample Input

rabcdeefgyYhFjkIoomnpOeorteeeeet
Sample Output

ee
Ioo
Oeo
eeeee
'''

import re
v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
# how to avoid overlapping issue
# (before)?<= ?<! (after)s?= ?! special structure and not consider as part of group
m = re.findall(r"(?<=[%s])([%s]{2,})[?=%s]" % (c, v, c), input(), flags = re.I)
print('\n'.join(m or ['-1']))