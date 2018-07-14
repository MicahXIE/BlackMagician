# Complete the solve function below.
'''
split() vs split(' ')
>>> lst = 'a      b      c'
>>> lst.split()
['a', 'b', 'c']
>>> lst.split(' ')
['a', '', '', '', '', '', 'b', '', '', '', '', '', 'c']

You are asked to ensure that the first and last names of people begin with a capital letter in their passports. 
For example, alison heck should be capitalised correctly as Alison Heck.
alison heck -> Alison Heck

Given a full name, your task is to capitalize the name appropriately.

Sample Input:
chris alan

Sample Output:
Chris Alan

'''


def solve(s):
    #solution 1
    #The method title() returns a copy of the string 
    #in which first characters of all the words are capitalized.
    #return s.title()
    
    #solution 2
    #It returns a copy of the string with only its first character capitalized.
    #lst = s.split(' ')
    #res = []
    #for e in lst:
    #    res.append(e.capitalize())
    #res_str = ' '.join(res)
    #return res_str
    
    #solution 3
    #lst = s.split(' ')
    #res = []
    #for e in lst:
    #    res.append(e[0].upper()+e[1:])
    #res_str = ' '.join(res)
    #return res_str

    #solution 4
    return ' '.join([st.capitalize() for st in s.split(' ')])

if __name__ == '__main__':

    s = input()

    result = solve(s)

    print(result)