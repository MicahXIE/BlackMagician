# what is the result. answer: [4,3]
a=[1,2,3,4,5]
print(a[3:1:-1])

#How to assign a tuple of length 1 to a
a=(1,) # correct answer, a=1, a=(1), a=tuple(1) all not correct

# what is the type of b: float, complex, int, str. answer: type(b) <class 'complex'>
a = -1
b = a ** 0.5

# what is the value of a: a = -4 / 1.5: 2.0,3.0,-2.0,-3.0, answer: -3.0
a = -4 // 1.5 # -3.0 
b = -4 / 1.5 # -2.6666666666666

# a = { i for i in range(0,10,2)}, is it syntax valid, answer: yes
a = { i for i in range(0,10,2) }
# a
# {0, 2, 4, 6, 8}
# type(a)
# <class 'set'>

# what is the value of a: a={1,2,3} < {2,3,4,5}, answer: False
a = {1,2,3} < {2,3,4,5}

# Opening a file in 'a' mode means: Opening a file for appending at the end of the file

# Which module is used for regular expressions: re or regex, answer is re

'''
write a function named to byte, which accepts an argument of either str or bytes and returns
the bytes value. You need to convert str to bytes otherwise just return bytes as it is
example:
string to bytes:
>>> s = '123'
>>> type(s)
<class 'str'>
>>> bytes(s,encoding='utf8')
b'123'

bytes to string:
>>> b = b'123'
>>> type(b)
<class 'bytes'>
>>> str(b, encoding = 'utf8')
'123'
'''
def toBytes(value):
	if type(value) == 'str':
		return bytes(value, encoding='utf8')
	else:
		return value

'''
write a program to exhibit the features of class named Employee
'''
# tbu


