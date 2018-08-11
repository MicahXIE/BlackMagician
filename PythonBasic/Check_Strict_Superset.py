'''
Input Format

The first line contains the space separated elements of set A. 
The second line contains integer n, the number of other sets. 
The next n lines contains the space separated elements of the other sets.

Output Format

Print True if set A is a strict superset of all other N sets. Otherwise, print False.

Sample Input 0

1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12
Sample Output 0

False
'''

A = set(map(int, input().strip().split()))
n = int(input().strip())
flag = 0
for _ in range(n):
    B = set(map(int, input().strip().split()))
    if B.issubset(A) and len(B) != len(A):
        flag = 1
    else:
        flag = 0
        break

if flag == 0:
    print('False')
if flag == 1:
    print('True')