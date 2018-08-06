'''
Input Format

The first line contains the space separated values of x and k. 
The second line contains the polynomial P.

Output Format

Print True if P(x) = k. Otherwise, print False.

Sample Input
1 4
x**3 + x**2 + x + 1

Sample Output
True

Explanation
P(1) = 1^3 + 1^2 + 1 + 1 = 4 =K
 
Hence, the output is True.

'''

if __name__ == '__main__':
    a,b = input().strip().split()
    p = input().strip().replace('x',a)

    #very strong function for eval
    res = eval(p)
    
    if int(b) == res:
        print("True")
    else:
        print("False")

