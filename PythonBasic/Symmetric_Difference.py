'''
Input Format

The first line of input contains an integer, . 
The second line contains  space-separated integers. 
The third line contains an integer, . 
The fourth line contains  space-separated integers.

Output Format

Output the symmetric difference integers in ascending order, one per line.

Sample Input

4
2 4 5 9
4
2 4 11 12
Sample Output

5
9
11
12

'''

m = int(input().strip())
m_lst = list(map(int, input().strip().split()))
m_set = set(m_lst)

n = int(input().strip())
n_lst = list(map(int, input().strip().split()))
n_set = set(n_lst)

m_n_diff = m_set.difference(n_set)
n_m_diff = n_set.difference(m_set)
m_n_union = m_n_diff.union(n_m_diff)

for i in sorted(m_n_union):
    print(i)