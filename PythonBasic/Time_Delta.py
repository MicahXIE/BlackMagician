'''
Sample Input:
2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000

Sample Output:
25200
88200

Explaination:
In the first query, when we compare the time in UTC for both the time stamps, 
we see a difference of 7 hours. which is 7x3600 seconds or 25200 seconds.

Similarly, in the second query, time difference is 5 hours and 
30 minutes for time zone adjusting for that we have a difference of 1 day and 30 minutes. Or 
24 x 3600 + 30 x 60 = 88200

# 格式化成2016-03-20 11:45:39形式
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
# 格式化成Sat Mar 28 22:24:24 2016形式
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

'''

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    d1=datetime.strptime(t1,'%a %d %b %Y %H:%M:%S %z')
    d2=datetime.strptime(t2,'%a %d %b %Y %H:%M:%S %z')
    print (int(abs((d1-d2).total_seconds())))
    return str(int(abs((d1-d2).total_seconds())))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
