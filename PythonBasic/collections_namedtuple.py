'''
Sample Input

TESTCASE 01

5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6   

Sample Output

TESTCASE 01

78.00

refer to tip.txt item 6

Note: 
1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet. 
2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)
'''

from collections import namedtuple
N = int(input().strip())
columns = ','.join(input().strip().split())
Student = namedtuple('Student', columns)
sum = 0
for _ in range(N):
    stu = Student(*input().strip().split())
    sum += int(stu.MARKS)

avg = sum / N
print(avg)
