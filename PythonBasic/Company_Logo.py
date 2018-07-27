#!/bin/python3
'''
Sample Input:
aabbbccde

Sample Output:
b 3
a 2
c 2

Explanation 0

Here, b occurs 3 times. It is printed first.
Both a and c occur 2 times. So, a is printed in the second line and c in the third line because a comes before c in the alphabet.

Note: The string S has at least 3 distinct characters.
'''


import math
import os
import random
import re
import sys
from collections import OrderedDict, Counter


class OrderedCounter(Counter, OrderedDict):
    pass

if __name__ == '__main__':
    s = sorted(input())
    s_dict = OrderedCounter(s)
    
    for item in s_dict.most_common(3):
        print(*item)

