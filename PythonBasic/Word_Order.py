'''
Input Format

The first line contains the integer,n. 
The next n lines each contain a word.

Output Format

Output 2 lines. 
On the first line, output the number of distinct words from the input. 
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

Sample Input
'''

# method 1 fail when submit code, still confused, guess due to the dictionary is not ordered
'''
from collections import Counter

if __name__ == '__main__':
    n = int(input().strip())
    
    word_lst = []
    for _ in range(n):
        word = input().strip()
        word_lst.append(word)
    
    word_dict = Counter(word_lst)
    
    #print(word_dict)
    print(len(word_dict))
    
    for x in word_dict.values():
        print(str(x), end=' ')
    #print(*word_dict.values())
'''

# method 2 works well
from collections import OrderedDict
#define empty ordered dictionary, which counts occurences
dict = OrderedDict()

for i in range(int(input())):
    #If input not in the dictionary, then add it
    #else increment the counter
    key = input()
    if not key in dict.keys():
        dict.update({key : 1})
        continue
    dict[key] += 1

print(len(dict.keys()))
print(*dict.values())