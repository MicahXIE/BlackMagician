'''
Valid email addresses must follow these rules:

It must have the username@websitename.extension format type.
The username can only contain letters, digits, dashes and underscores.
The website name can only have letters and digits.
The maximum length of the extension is 3.

Sample Input

3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com
Sample Output

['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']

'''
import re

# method 1
def fun(s):
    # return True if s is a valid email, else return False
    try:
        username, url = s.split('@')
        website, extension = url.split('.')
    except ValueError:
        return False
    
    if not username.replace("-", "").replace("_", "").isalnum():
        return False
    if not website.isalnum():
        return False
    if len(extension) > 3:
        return False
    
    return True


# method 2
def fun2(s):
    a = re.match(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$',s)
    return(a)


def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

