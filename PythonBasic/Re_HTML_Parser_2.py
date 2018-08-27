'''
Sample Input

4
<!--[if IE 9]>IE9-specific content
<![endif]-->
<div> Welcome to HackerRank</div>
<!--[if IE 9]>IE9-specific content<![endif]-->
Sample Output

>>> Multi-line Comment
[if IE 9]>IE9-specific content
<![endif]
>>> Data
 Welcome to HackerRank
>>> Single-line Comment
[if IE 9]>IE9-specific content<![endif]
'''

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        comment_lst = data.strip().split('\n')
        if len(comment_lst) == 1:
            print(">>> Single-line Comment")
            print(comment_lst[0])
        if len(comment_lst) > 1:
            print(">>> Multi-line Comment")
            print(*comment_lst, sep='\n')

    def handle_data(self, data):
        data_lst = data.split('\n')
        if data_lst[0] != '':
            print(">>> Data")
            print(*data_lst, sep='\n')

html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

