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


def printx1(size, flag, lst = []):

	num = int(size//2) + 1
	str1 = ''

	for k in range(num):
		if (k % 2 == 0):
			str1 += 'x '
		else:
			str1 += 'o '

	lst.append(str1)

	if (flag == 0):

		str2 =' '
		for m in range(num):
			if (m % 2 == 0):
				str2 += 'x '
			else:
				str2 += 'o '

		lst.append(str2)

	return lst

def printo1(size, flag, lst=[]):

	num = int(size//2) + 1
	str1 = ''

	for k in range(num):
		if (k % 2 == 0):
			str1 += 'o '
		else:
			str1 += 'x '

	lst.append(str1)

	if (flag == 0):
		str2 =' '

		for m in range(num):
			if (m % 2 == 0):
				str2 += 'o '
			else:
				str2 += 'x '
		lst.append(str2)

	return lst

'''
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
'''
def print_pyramid1(size):
	#indicate the last line
	flag=0
	L=[]

	for i in range(0, size, 2):
		if (size % 2 != 0 and i == (size-1)):
			flag = 1

		if (i%4 == 0):
			L = printx1(i,flag,L)           
		else:
			L =printo1(i,flag,L)

		#print("list: ", L)

	# remove the last space in the list
	L1 = [s[:-1] for s in L]
	print(L1)
	print('\n'.join(L1))

    # make the symmetrical pyramid of L
	L2 = [s[::-1] for s in L1]	
	l2_len = len(L2)
	for i in range(l2_len):
		L2[i] = (l2_len-1-i)*' '+L2[i]

    # make the diagnal pyramid of L
	L3 = L2[::-1];
	print(L3)
	print('\n'.join(L3))
	print()

	for j in range(len(L1)):
		if(j == (len(L1)-1)):
			L1[j] = L3[0]+L1[j][1:]
			break
		L1[j] = (size-1)*' '+L1[j]


	print(L1)
	print(L3[1:])
	print('\n'.join(L1+L3[1:]))


if __name__ == '__main__':
    n = int(input())
    #print_rangoli(n)
    #print_pyramid(n)
    print_pyramid1(n)
