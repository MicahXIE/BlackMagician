'''
Sample Input 0

100,000,000.000
Sample Output 0

100
000
000
000
'''

regex_pattern = r"[,.]"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))


