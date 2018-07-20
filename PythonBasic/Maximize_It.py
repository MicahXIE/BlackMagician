'''
You are given a function f(x) = x^2. You are also given K lists. The i(th) list consists of N(i) elements.

You have to pick one element from each list so that the value from the equation below is maximized: 

S = (f(x1) + f(x2) + ... + f(xk)) % M

x(i) denotes the element picked from the i(th) list . Find the maximized value Smax obtained.

% denotes the modulo operator.

Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares of 
the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem.

Input Format

The first line contains 2 space separated integers K and M. 
The next K lines each contains an integer N(i), denoting the number of elements in the i(th) list, followed by N(i) space separated integers denoting the elements in the list.

Sample Input:
3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 

Sample Output:
206
'''

import itertools

if __name__ == "__main__":
    K, M = map(int, input().split())
    
    lst2 = []
    for _ in range(K):
        lst = list(map(int, input().split()))
        lst2.append(lst[1:])
    
    s_max = 0
    l_max = None
    
    # very useful tips for two-dimension list
    for l in itertools.product(*lst2):
        s = sum([x**2 for x in l]) % M
        
        if s > s_max:
            s_max = s
            l_max = l
    

    print(l_max, s_max)