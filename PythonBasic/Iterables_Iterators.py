'''
Sample Input
4 
a a c d
2

Sample Output
0.8333

Explanation

All possible unordered tuples of length 2 comprising of indices from 1 to 4 are:
(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)

Out of these 6 combinations, 5 of them contain either index 1 or index 2 which are the indices that contain the letter 'a'.

Hence, the answer is 5/6.

>> from itertools import combinations, permutations
>> permutations([1, 2, 3], 2)
<itertools.permutations at 0x7febfd880fc0>
                # 可迭代对象
>> list(permutations([1, 2, 3], 2))
[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

>> list(combinations([1, 2, 3], 2))
[(1, 2), (1, 3), (2, 3)]


'''

from itertools import permutations,combinations

if __name__ == '__main__':
    N = int(input().strip())
    
    num_lst = [x for x in range(1,N+1)]
    
    letters_lst = list(input().strip().split())
    
    K = int(input().strip())
    
    res_lst = list(combinations(num_lst, K))
    
    total = len(res_lst)
    count = 0
    
    for item in res_lst:
        for e in item:
            if letters_lst[e-1] == 'a':
                count += 1
                break
    
    print(count/total)

