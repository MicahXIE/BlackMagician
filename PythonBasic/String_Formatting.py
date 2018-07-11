'''
# 位置参数
print "{0} is {1} years old".format("Wilber", 28)
print "{} is {} years old".format("Wilber", 28)
print "Hi, {0}! {0} is {1} years old".format("Wilber", 28)

# 关键字参数
print "{name} is {age} years old".format(name = "Wilber", age = 28)

# 下标参数
li = ["Wilber", 28]
print "{0[0]} is {0[1]} years old".format(li)

# 填充与对齐
# ^、<、>分别是居中、左对齐、右对齐，后面带宽度
# :号后面带填充的字符，只能是一个字符，不指定的话默认是用空格填充

#python 3
>>> print('{:>8}'.format('3.14'))
    3.14
>>> print('{:<8}'.format('3.14'))
3.14    
>>> print('{:^8}'.format('3.14'))
  3.14  
>>> print('{:0>8}'.format('3.14'))
00003.14
>>> print('{:a>8}'.format('3.14'))
aaaa3.14
>>> print('{:>8}'.format(3.14))
    3.14

# 浮点数精度
print '{:.4f}'.format(3.1415926)
print '{:0>10.4f}'.format(3.1415926)

# 进制
# b、d、o、x分别是二进制、十进制、八进制、十六进制
print '{:b}'.format(11)
print '{:d}'.format(11)
print '{:o}'.format(11)
print '{:x}'.format(11)
print '{:#x}'.format(11)
print '{:#X}'.format(11)

2,3 keep the fixed positions

>>> print('{:2d}'.format(11))
11
>>> print('{:2d}'.format(2))
 2

>>> print('{:2X}'.format(11))
 B
>>> print('{:3X}'.format(11))
  B

# 千位分隔符
print '{:,}'.format(15700000000)

Task:

Given an integer,n, print the following values for each integer i from 1 to n:

1. Decimal
2. Octal
3. Hexadecimal (capitalized)
4. Binary
The four values must be printed on a single line in the order specified above for each i from 1 to n. 
Each value should be space-padded to match the width of the binary value of n.

Sample input:
2

Sample output:

 1  1  1  1
 2  2  2 10
'''
#Solution 1:
def print_formatted_s1(number):
    w = len(format(number, 'b'))
    for i in range(1, number+1):
        d = str(i).rjust(w)
        o = format(i, 'o').rjust(w)
        h = format(i, 'x').rjust(w).upper()
        b = format(i, 'b').rjust(w)
        print(d, o, h, b)

#Solution 2
def print_formatted_s2(number):
    width = len("{0:b}".format(number))
    for i in range(1, number+1):
        print("{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}".format(i=i, width=width))
        

if __name__ == '__main__':
    n = int(input())
    print_formatted_s2(n)



