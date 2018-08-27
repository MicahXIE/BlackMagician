'''
Sample Input

9
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">
  <!-- <param name="movie" value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>
Sample Output

head
title
object
-> type > application/x-flash
-> data > your-file.swf
-> width > 0
-> height > 0
param
-> name > quality
-> value > high

'''

from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        if attrs:
            for item in attrs:
                print("-> "+item[0]+" > "+str(item[1]))
    #def handle_endtag(self, tag):
    #    print(tag)
    def handle_startendtag(self, tag, attrs):
        print(tag)
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
