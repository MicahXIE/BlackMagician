'''
Sample Input

2
<html><head><title>HTML Parser - I</title></head>
<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>
Sample Output

Start : html
Start : head
Start : title
End   : title
End   : head
Start : body
-> data-modal-target > None
-> class > 1
Start : h1
End   : h1
Empty : br
End   : body
End   : html
'''

from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        if attrs:
            for item in attrs:
                print("-> "+item[0]+" > "+str(item[1]))
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        if attrs:
            for item in attrs:
                print("-> "+item[0]+" > "+str(item[1]))

# instantiate the parser and fed it some HTML
n = int(input())
s = ''''''
for _ in range(n):
    s += input().strip()

parser = MyHTMLParser()
parser.feed(s)