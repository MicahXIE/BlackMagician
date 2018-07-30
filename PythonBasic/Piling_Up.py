'''
There is a horizontal row of n cubes. The length of each cube is given. You need to create a new vertical pile of cubes. 
The new pile should follow these directions: if cube(i) is on top of cube(j) then sideLength(j) > sideLength(i). 
When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print "Yes" 
if it is possible to stack the cubes. Otherwise, print "No". Do not print the quotation marks.

Input Format

The first line contains a single integer T, the number of test cases. 
For each test case, there are 2 lines. 
The first line of each test case contains n, the number of cubes. 
The second line contains n space separated integers, denoting the sideLengths of each cube in that order.

Sample Input
2
6
4 3 2 1 3 4
3
1 3 2

Sample Output:
Yes
No

'''


def piling_up(lst):
    start = 0
    end = len(lst)-1
    top = 0
    
    while(start < end):
        if lst[end] > lst[start] :
            if top > 0 and top < lst[end]:
                return False
            top = lst[end]
            end -= 1
        else:
            if top > 0 and top < lst[start] :
                return False
            top = lst[start]
            start += 1
    
    return True

if __name__ == '__main__':
    n = int(input().strip())
    
    for i in range(n):
        num = int(input().strip())
        cube_lst = list(map(int, input().strip().split()))
        res = piling_up(cube_lst)
        if res:
            print("Yes")
        else:
            print("No")