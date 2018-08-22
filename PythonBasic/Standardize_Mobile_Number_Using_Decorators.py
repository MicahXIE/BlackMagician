'''
Input Format

The first line of input contains an integer N, the number of mobile phone numbers. 
N lines follow each containing a mobile number.

Output Format

Print N mobile numbers on separate lines in the required format.

Sample Input

3
07895462130
919875641230
9195969878
Sample Output

+91 78954 62130
+91 91959 69878
+91 98756 41230
'''

def wrapper(f):
    def fun(l):
        # complete the function
        lst = []
        for str in l:
            lst.append('+91'+' '+str[-10:-5]+' '+str[-5:])
        f(lst)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 