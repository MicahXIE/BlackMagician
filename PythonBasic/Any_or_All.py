'''
Sample Input

5
12 9 61 5 14 
Sample Output

True

Explanation

Condition 1: All the integers in the list are positive. 
Condition 2: Any element is a palindromic integer.
'''

n = int(input().strip())
lst = input().strip().split()
print(all([int(i)>0 for i in lst]) and any(j==j[::-1] for j in lst))

