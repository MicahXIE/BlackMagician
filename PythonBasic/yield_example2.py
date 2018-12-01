def g():
    print('1')
    x=yield 'hello'
    print('2 x=', x)
    y=5+(yield x)
    print('3 y=', y)

f=g()
next(f)
f.send(5)
f.send(2)

'''
Matthews-MacBook-Pro:PythonBasic matthew$ python3 yield_example2.py 
1
2 x= 5
3 y= 7
Traceback (most recent call last):
  File "yield_example2.py", line 11, in <module>
    f.send(2)
StopIteration
'''


