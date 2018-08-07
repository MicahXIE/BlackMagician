'''
Sample Input 0

3
odd 2
even 3
odd 5
Sample Output 0

1
3
0
2
4
1
3
5
7
9
'''
class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return


'''
wrong example:
def print_from_stream(n, stream=EvenStream()):
    
    for _ in range(n):
        print(stream.get_next())

explaination:
the right hand side of the default argument, the EvenStream() in stream=EvenStream(), 
is only constructed once, when the function is defined. Further calls to that function 
will use that initial instance instead of creating a new EvenStream() every time.
'''

def print_from_stream(n, stream=None):
    if stream == None:
        stream = EvenStream()
    
    for _ in range(n):
        print(stream.get_next())


queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())

