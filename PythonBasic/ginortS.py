'''
You are given a string S. 
All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.

Sample Input

Sorting1234
Sample Output

ginortS1324

Explore the lambda solution and understand multiple sorting rules in lambda key

'''

s = input().strip()

s_lower = ''
s_upper = ''
s_odd = ''
s_even = ''

for c in s:
    if c.islower():
        s_lower += c
    if c.isupper():
        s_upper += c
    if c.isdigit():
        if int(c)%2 == 0:
            s_even += c
        else:
            s_odd += c

res = ''.join(sorted(s_lower)) + ''.join(sorted(s_upper)) + ''.join(sorted(s_odd)) + ''.join(sorted(s_even))

print(res)