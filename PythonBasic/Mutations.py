'''
We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).
You are given an immutable string, and you want to make changes to it.

>>> string = "abracadabra"
>>> l = list(string)
>>> l[5] = 'k'
>>> string = ''.join(l)
>>> print string
abrackdabra


>>> string = string[:5] + "k" + string[6:]
>>> print string
abrackdabra

'''

def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

