'''
Sample Input

08 05 2015
Sample Output

WEDNESDAY
'''
'''
strptime = "string parse time"
strftime = "string format time"
'''

from datetime import datetime

if __name__ == '__main__':
    dt = datetime.strptime(input().strip(), '%m %d %Y')
    print(dt.strftime('%A').upper())
