'''
A valid postal code P have to fullfil both below requirements:

 P must be a number in the range from 100000 to 999999 inclusive.
 P must not contain more than one alternating repetitive digit pair.

121426 # Here, 1 is an alternating repetitive digit.
523563 # Here, NO digit is an alternating repetitive digit.
552523 # Here, both 2 and 5 are alternating repetitive digits.

Sample Input:
110000

Sample Output:
False

reference
http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html

(?:abc){2}  ---> abcabc
(?i)abc     ---> AbC
a(?=\d)     ---> a1 a2
a(?!\d)     ---> ab ac

'''
regex_integer_in_range = r"^[1-9][0-9]{5}$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"

import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)