'''
There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. 
You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0. 
For each i integer in the array, if i belong to A , you add 1 to your happiness. If i belong to B , 
you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.

Input Format

The first line contains integers n and m separated by a space. 
The second line contains n integers, the elements of the array. 
The third and fourth lines contain m integers, A and B, respectively.

Output Format

Output a single integer, your total happiness.

Sample Input:
3 2
1 5 3
3 1
5 7

Sample Output:
1

'''

if __name__ == "__main__":
    N, K = map(int, input().strip().split())
    lst = list(map(int, input().strip().split()))
    A = set(map(int,input().strip().split()))
    B = set(map(int,input().strip().split()))
    
    # method 1
    #happiness = 0
    #for e in lst:
    #    if e in A:
    #        happiness += 1
    #    if e in B:
    #        happiness -= 1
    #print(happiness)
    
    # method 2
    #print(sum([1 if x in A else -1 if x in B else 0 for x in lst]))

    # method 3
    print(sum([(x in A) - (x in B) for x in lst]))
