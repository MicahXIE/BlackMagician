'''
Input Format

The first line contains a single string denoting s. 
The second line contains an integer, k, denoting the length of each subsegment.

Constraints

1 <= n <= 10^4, where n is the length of s
1 <= k <= n 
It is guaranteed that n is a multiple of k.


Output Format

Print n/k lines where each line i contains string u(i).



Sample Input:
AABCAAADA
3

Sample Output:
AB
CA
AD

Explanation:

String s is split into n/k = 9/3 = 3  equal parts of length k = 3 . We convert each t(i) to u(i) 
by removing any subsequent occurrences non-distinct characters in t(i):

1. t(0) = "AAB" -> u(0) = "AB"
2. t(1) = "CAA" -> u(1) = "CA"
3. t(2) = "ADA" -> u(2) = "AD"

We then print each u(i) on a new line.

'''
def merge_the_tools_s1(string, k):
    # your code goes here
    n = len(string)
    t = int(n/k)
    
    s_lst = list(string)
    
    for i in range(1,t+1):
        s1_lst = s_lst[(i-1)*k:(i*k-1)+1]

        #remove the duplicated element
        s2_lst = list(set(s1_lst))
        
        #return to  the original position
        s2_lst.sort(key=s1_lst.index)
        
        print(''.join(s2_lst))

def merge_the_tools_s2(string, k):
	l = len(string)//k

	for i in range(l):
		t = ''
		for c in string[i*k:(i+1)*k]:
			# good example for remove duplicated
			if c not in t: t+=c
		print(t)

if __name__ == '__main__':
	string, k = input(), int(input())
	merge_the_tools_s2(string, k)




