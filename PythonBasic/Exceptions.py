'''
Sample Input

3
1 0
2 $
3 1
Sample Output

Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3
Note: 
For integer division in Python 3 use //.
'''

if __name__ == '__main__':
    num = int(input().strip())
    
    for _ in range(num):
        try:
            a,b = map(int, input().strip().split())
            print(a//b)
        except ValueError as e:
            print("Error Code:",e)
        except ZeroDivisionError as e:
            print("Error Code:",e)