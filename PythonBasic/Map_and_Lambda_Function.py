
'''
Sample Input

5
Sample Output

[0, 1, 1, 8, 27]
Explanation

The first 5 fibonacci numbers are [0,1,1,2,3], and their cubes are [0,1,1,8,27].
'''

cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    lst = []
    for i in range(n):
        if i == 0:
            lst.append(0)
        if i == 1:
            lst.append(1)
        if i >=2:
            lst.append(lst[i-1]+lst[i-2])
    return lst

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))