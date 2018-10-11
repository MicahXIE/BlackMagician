'''
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

    x                                   
     x 
    o x 
     o x 
x o x o x 
 x o 
  x o 
   x 
    x 

x

 x
x x
 x

   x
    x
 x o x
  x
   x

   x
    x
   o x
x o o x
 x o
  x
   x


    x
     x
    o x
     o x
x o x o x
 x o
  x o
   x
    x

     x
      x
     o x
      o x
     x o x
x o x x o x
 x o x
  x o
   x o
    x
     x

https://www.hackerrank.com/challenges/text-alignment/problem
'''

import string

def print_rangoli(size):
    alpha = string.ascii_lowercase
    
    L = []
    for i in range(size):
        s = "-".join(alpha[i:size])
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    print('\n'.join(L[:0:-1]+L))


def printx(size, flag):

	num = int(size//2) + 1

	for k in range(num):
		if (k % 2 == 0):
			print('x ', end='')
		else:
			print('o ', end='')

	if (flag == 0):
		print()
		print(' ', end='')

		for m in range(num):
			if (m % 2 == 0):
				print('x ', end='')
			else:
				print('o ', end='')


def printo(size, flag):

	num = int(size//2) + 1

	for k in range(num):
		if (k % 2 == 0):
			print('o ', end='')
		else:
			print('x ', end='')


	if (flag == 0):
		print()
		print(' ',end='')

		for m in range(num):
			if (m % 2 == 0):
				print('o ', end='')
			else:
				print('x ', end='')

'''
this function is used to print below part:

x
 x
o x
 o x
x o x
 x o x
'''
def print_pyramid(size): 
	#indicate the last line
	flag=0

	for i in range(0, size, 2):
		if (size % 2 != 0 and i == (size-1)):
			flag = 1

		if (i%4 == 0):
			printx(i,flag)           
		else:
			printo(i,flag)
		print()



if __name__ == '__main__':
    n = int(input())
    #print_rangoli(n)
    print_pyramid(n)
